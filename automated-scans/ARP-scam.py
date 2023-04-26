from scapy.all import ARP, Ether, srp

# Define the target IP address
target_ip = "**.*.*.**"

# Create an ARP request packet
arp = ARP(pdst=target_ip)

# Create an Ethernet frame
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# Combine the ARP and Ethernet packets
packet = ether/arp

# Send the packet and capture the response
result = srp(packet, timeout=3, verbose=0)[0]

# Print the result
print("IP\t\tMAC Address\n--------------------------")
for sent, received in result:
    print(received.psrc + "\t" + received.hwsrc)
