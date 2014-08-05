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

from subprocess import PIPE, Popen
import time

def spawnTrem():
	p = Popen(["/home/yarou/Downloads/tremulous/tremulous-tty", "+connect 69.9.166.166:30720"], stdin=PIPE, stdout=PIPE)
	sleep(10)