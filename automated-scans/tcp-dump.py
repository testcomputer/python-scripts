import subprocess

# Capture packets with tcpdump
subprocess.call(['tcpdump', '-i', 'eth0', '-w', 'packets.pcap'])

# Analyze packets with scapy
from scapy.all import *

packets = rdpcap('packets.pcap')

# Filter packets by protocol and port number
filtered_packets = packets.filter(lambda pkt: TCP in pkt and (pkt[TCP].sport == 80 or pkt[TCP].dport == 80))

# Print summary of filtered packets
print("Filtered packets:")
print(filtered_packets.summary())

# Analyze packet contents for potential issues
for pkt in filtered_packets:
    # Check for malformed packets
    if pkt.haslayer(Raw):
        print("Malformed packet detected: ")
        print(pkt.show())

    # Check for unusual packet size
    if len(pkt) < 64:
        print("Small packet detected: ")
        print(pkt.show())

    # Check for unusual packet timing
    if pkt.time - filtered_packets[0].time > 1:
        print("Delay detected between packets: ")
        print(pkt.show())

# Identify potential root cause of network issue based on packet analysis
# For example, if there are many malformed packets, the issue could be with the network hardware or configuration.



# we're capturing packets with tcpdump and analyzing them with scapy. We're filtering the packets by protocol and
# port number to focus on HTTP traffic, and then checking for potential issues such as malformed packets, small packets,
# and delays between packets. Based on the results of the analysis, we can identify potential root causes of the network
# issue and take appropriate action to resolve it.
