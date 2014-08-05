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
