from twisted.words.protocols import irc
from twisted.internet import protocol

class ServerSpy(irc.IRCClient):
	def _get_nick(self):
		return self.factory.nickname
	nickname = property(_get_nickname)

	def signedOn(self):
		self.join(self.factory.channel)
		print "Signed on as %s" % (self.nickname,)

	def privmsg(self,user, channel, msg)
		print msg

class ServerSpyFactory(protocol.ClientFactory):
	protocl = ServerSpy

	def __init__(self, channel, nickname='ServerSpy'):
		self.channel = channel
		self.nickname = nickname

	def clientConnectionLost(self, connector, reason):
		print "Connection lost (%s), reconnecting." % (reason,)
		connector.connect()
	def clientConnectionFailed(self, connector, reason):
		print "Couldn't connect: %s" % (reason,)