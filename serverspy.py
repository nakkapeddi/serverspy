#ServerSpy
#Copyright (c) 2014, Naveen Akkapeddi <naveen.csci@gmail.com>, All rights reserved.
#
#This library is free software; you can redistribute it and/or
#modify it under the terms of the GNU Lesser General Public
#License as published by the Free Software Foundation; either
#version 3.0 of the License, or (at your option) any later version.
#
#This library is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#Lesser General Public License for more details.

#You should have received a copy of the GNU Lesser General Public
#License along with this library.
import time
import subprocess
import sys
from twisted.words.protocols import irc
from twisted.internet import protocol, reactor, task, threads
from subprocess import PIPE, Popen

buffer = ""

def spawnTrem():
	global p
	p = Popen(["/home/yarou/Downloads/tremulous/tremulous-tty", "+connect 69.9.166.166:30720"], stdin=PIPE, stdout=PIPE)

#def spawnReader():
#	buffer = p.stdout.readline()

class ServerSpy(irc.IRCClient):
	def _get_nickname(self):
		return self.factory.nickname
	nickname = property(_get_nickname)

	def signedOn(self):
		self.join(self.factory.channel)
		print "Signed on as %s" % (self.nickname,)
#		lt = task.LoopingCall(self._clientpeek)
#		lt.start(10)

	def joined(self, channel):
		print "Joined channel"

	def privmsg(self,user, channel, msg):
		ircNick = user.split('!', 1)[0]
		if msg[0] == '@' and ircNick == 'Yarou':
			p.stdin.write('/' + msg[1:] + '\n')
		else:
			p.stdin.write('/say ' + '^7<' + ircNick + '@IRC> ' + msg + '\n')

#	def _clientpeek(self):
#		self.msg(self.factory.channel, buffer)

class ServerSpyFactory(protocol.ClientFactory):
	protocol = ServerSpy

	def __init__(self, channel, nickname='ServerSpy'):
		self.channel = channel
		self.nickname = nickname

	def clientConnectionLost(self, connector, reason):
		print "Connection lost (%s), reconnecting." % (reason,)
		connector.connect()
	def clientConnectionFailed(self, connector, reason):
		print "Couldn't connect: %s" % (reason,)

def scheduler():
	reactor.callFromThread(spawnTrem)

if __name__ == "__main__":
	chan = sys.argv[1]
	reactor.connectTCP('irc.freenode.net', 6667, ServerSpyFactory('#' + chan))
	scheduler()
	reactor.run()
