#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help=" Interface to change its MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help=" New MAC-address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please input the name interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("Please input the new mac, use --help for more info.")
    return options


# interface = input(str("Input the interface:  "))
# new_mac = input("Input the new MAC-address (00:00:00:00:00:00):  ")
# print("[+]  Changing MAC-address for", interface, "to", new_mac)


def mac_changer(interface, new_mac):
    print("The current MAC-address: "); subprocess.call("ifconfig " + options.interface + " | grep ether", shell=True)

    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
    print("MAC-address successfully has changed to: ")
    subprocess.call("ifconfig " + options.interface + " | grep ether", shell=True)
#    subprocess.check_output("ifconfig " + options.interface)     #this code line as like to 28th line

options = get_arguments()
mac_changer(options.interface, options.new_mac)