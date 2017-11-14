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
c2 = net.addController('c2', controller=RemoteController, ip="192.168.56.101", port=7753)
c3 = net.addController('c3', controller=RemoteController, ip="192.168.56.101", port=8853)
c4 = net.addController('c4', controller=RemoteController, ip="192.168.56.101", port=9953)
  
print "*** Creating switches"
s1 = net.addSwitch( 's1',protocols="OpenFlow14" )
s2 = net.addSwitch( 's2',protocols="OpenFlow14" )
s3 = net.addSwitch( 's3',protocols="OpenFlow14" )
s4 = net.addSwitch( 's4',protocols="OpenFlow14" )
s5 = net.addSwitch( 's5',protocols="OpenFlow14" )
s6 = net.addSwitch( 's6',protocols="OpenFlow14" )
s7 = net.addSwitch( 's7',protocols="OpenFlow14" )
s8 = net.addSwitch( 's8',protocols="OpenFlow14" )
s9 = net.addSwitch( 's9',protocols="OpenFlow14" )
s10 = net.addSwitch( 's10',protocols="OpenFlow14" )
  
print "*** Creating hosts"
hosts1 = [ addHost( net, n ) for n in range(1, 5) ]
hosts2 = [ addHost( net, n ) for n in range(6, 10) ]
hosts3 = [ addHost( net, n ) for n in range(11, 15) ]
hosts4 = [ addHost( net, n ) for n in range(16, 20) ]
hosts5 = [ addHost( net, n ) for n in range(21, 25) ]
hosts6 = [ addHost( net, n ) for n in range(26, 30) ]
hosts7 = [ addHost( net, n ) for n in range(31, 35) ]
hosts8 = [ addHost( net, n ) for n in range(36, 40) ]
hosts9 = [ addHost( net, n ) for n in range(41, 45) ]
hosts10 = [ addHost( net, n ) for n in range(46, 50) ]
  
print "*** Creating links"
for h in hosts1:
    s1.linkTo( h )
for h in hosts2:
    s2.linkTo( h )
for h in hosts3:
    s3.linkTo( h )
for h in hosts4:
    s4.linkTo( h )
for h in hosts5:
    s5.linkTo( h )
for h in hosts6:
    s6.linkTo( h )
for h in hosts7:
    s7.linkTo( h )
for h in hosts8:
    s8.linkTo( h )
for h in hosts9:
    s9.linkTo( h )
for h in hosts10:
    s10.linkTo( h )
  
s1.linkTo( s2 )
s2.linkTo( s3 )
s3.linkTo( s4 )
s4.linkTo( s5 )
s5.linkTo( s6)
s6.linkTo( s7 )
s7.linkTo( s8 )
s8.linkTo( s9 )
s9.linkTo( s10 )
  
print "*** Building network"
net.build()
  
# In theory this doesn't do anything
c1.start()
c2.start()
c3.start()
c4.start()
  
#print "*** Starting Switches"
s1.start( [c1,c2,c3,c4] )
s2.start( [c1,c2,c3,c4] )
s3.start( [c1,c2,c3,c4] )
s4.start( [c1,c2,c3,c4] )
s5.start( [c1,c2,c3,c4] )
s6.start( [c1,c2,c3,c4] )
s7.start( [c1,c2,c3,c4] )
s8.start( [c1,c2,c3,c4] )
s9.start( [c1,c2,c3,c4] )
s10.start( [c1,c2,c3,c4] )

net.start()
CLI(net)
