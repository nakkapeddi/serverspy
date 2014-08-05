import sys
from twisted.internet import reactor
from serverspy import *
from serverspytrem import *

def scheduler():
	reactor.callFromThread(spawnTrem)

if __name__ == "__main__":
	chan = sys.argv[1]
	reactor.connectTCP('irc.freenode.net', 6667, ServerSpyFactory('#' + chan))
	scheduler()
	reactor.run()
