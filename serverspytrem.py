from subprocess import PIPE, Popen
import time

def spawnTrem():
	p = Popen(["/home/yarou/Downloads/tremulous/tremulous-tty", "+connect 69.9.166.166:30720"], stdin=PIPE, stdout=PIPE)
	sleep(10)