#!/usr/bin/python

from scapy.all import *
import time,threading

count=0
while(True):
	count+=1
	scr = "10.0.0.1"
	dst = RandIP()
	sPort = 12345
	dPort = 5556
	send(IP(src=scr,dst=dst)/UDP(sport=sPort,dport=dPort))
	print(count)

