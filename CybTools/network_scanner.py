#!/usr/bin/env python

import scapy.all as scapy
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()                                                            #   also we can use "argparse"
    parser.add_option("--na", dest="network", help=" Network address for scanning")
    (options, arguments) = parser.parse_args()
    if not options.network:
        parser.error("Please input the network address, use --help for more info.")
    return options

options = get_arguments()



def scan(ip):
#     scapy.arping(ip)                          # check ip in local network
    arp_request = scapy.ARP(pdst=ip)            # creating ARP-requests to hosts
#     print(arp_request.summary())              # definition of action arp_request()
#     arp_request.pdst = ip                     # pdst - is ip parameter of scapy.ARP()  and we specify it in function scapy.ARP()
                                                # and also we can specify arp_request.pdst = ip in, as scapy.ARP(pdst = ip)
#      scapy.ls(scapy.ARP())                    # lists all parameters of scapy.ARP()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     print(broadcast.summary())
#     scapy.ls(scapy.Ether())
    arp_request_broadcast = broadcast/arp_request                                           #   execution 2 commnads in one time
#    arp_request_broadcast.show()                                                           #   show and print the result

    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]                #   assigning the 2-nd resieved request in variable "answered"
# "verbose" cleans unnecessary entries
    clients_list = []
    for element in answered:                                                                #   by using "for", we print the lines that we need
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}                      #   to print "ip" and "MAC"
        clients_list.append(client_dict)
    return clients_list

def print_result(result_list):
    print("------------------------------------------------------------\nIP \t\t\t MAC")
    for client in result_list:
        print(client["ip"], "\t\t", client["mac"])

scan_result = scan(options.network)
print_result(scan_result)