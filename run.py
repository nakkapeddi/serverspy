import sys
from twisted.internet import reactor
from serverspy import *

if __name__ == "__main__":
	chan = sys.argv[1]
	reactor.connectTCP('irc.freenode.net', 6667, ServerSpyFactory('#' + chan))
	reactor.run()