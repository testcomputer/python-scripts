# Requires netifaces module(package) to be installed

# !! Run 'pip install netifaces' before running this script !!

import netifaces

# get a list of all network interfaces
interfaces = netifaces.interfaces()

# loop through the interfaces and print their information
for interface in interfaces:
    addrs = netifaces.ifaddresses(interface)
    print(f"Interface: {interface}")
    for family in addrs:
        print(f"\tFamily: {netifaces.address_families[family]}")
        for addr in addrs[family]:
            if "addr" in addr:
                print(f"\t\tAddress: {addr['addr']}")
            if "broadcast" in addr:
                print(f"\t\tBroadcast: {addr['broadcast']}")

# This script creates legible output for your network configuration

# Go buck wild!
