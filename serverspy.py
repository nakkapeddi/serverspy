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

from twisted.words.protocols import irc
from twisted.internet import protocol

class ServerSpy(irc.IRCClient):
	def _get_nickname(self):
		return self.factory.nickname
	nickname = property(_get_nickname)

	def signedOn(self):
		self.join(self.factory.channel)
		print "Signed on as %s" % (self.nickname,)

	def privmsg(self,user, channel, msg):
		print msg

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
