import nmap
import pprint

# Create an Nmap scanner object
scanner = nmap.PortScanner()

# Define the target IP address
target_ip = "[TARGET-IP-ADDRESS]"

# Run an Nmap scan against the target IP
print("Running Nmap scan...")
scanner.scan(target_ip, arguments="-sS -p -F -T4 -A -v -oN TestScanScript.txt")

# Run a vulnerability scan against the target IP
print("Running vulnerability scan...")
scanner.scan(target_ip, arguments="--script vuln -oN TestScanScript.txt")

# Print the scan results
pprint.pprint(scanner.all_hosts())
pprint.pprint(scanner[target_ip].hostname())
pprint.pprint(scanner[target_ip].state())
pprint.pprint(scanner[target_ip].all_protocols())
pprint.pprint(scanner[target_ip]['tcp'].keys())

# Save the scan results to a file
with open("TestScanScript.txt", "w") as f:
    f.write(scanner.csv())
