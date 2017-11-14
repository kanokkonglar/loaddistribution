#!/usr/bin/python                                                                                                                                                                  
import time
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info,output
  
setLogLevel('info')
  
def addHost(net, N):
    name= 'h%d' % N
    ip = '10.0.0.%d' % N
    return net.addHost(name, ip=ip)
  
net = Mininet(controller=RemoteController, switch=OVSSwitch)
c1 = net.addController('c1', controller=RemoteController, ip="192.168.56.101", port=6653)
  
print "*** Creating switches"
s1 = net.addSwitch( 's1',protocols="OpenFlow14" )
s2 = net.addSwitch( 's2',protocols="OpenFlow14" )

print "*** Creating hosts"
hosts1 = [ addHost( net, n ) for n in range(1, 5) ]
hosts2 = [ addHost( net, n ) for n in range(6, 9) ]
  
print "*** Creating links"
for h in hosts1:
    s1.linkTo( h )
for h in hosts2:
    s2.linkTo( h )

  
s1.linkTo( s2 )

  
print "*** Building network"
net.build()
  
# In theory this doesn't do anything
c1.start()

#print "*** Starting Switches"
s1.start( [c1] )
s2.start( [c1] )

net.start()
CLI(net)
