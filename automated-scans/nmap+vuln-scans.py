import nmap

# For Windows OS, install python-nmap via "pip install python-nmap"
# Create an Nmap scanner object
scanner = nmap.PortScanner()

# Define the target IP address
target_ip = "[TARGET-IP-ADDRESS]"

# Run an Nmap scan against the target IP
# Scan all 65,535 ports, (Reduce for faster results)
# Saves output as "TestScanScript.txt"
print("Running Nmap scan...")
scanner.scan(target_ip, arguments="-sS -p 1-65535 -T4 -A -v -oN TestScanScript.txt")

# Run a vulnerability scan against the target IP
print("Running vulnerability scan...")
scanner.scan(target_ip, arguments="--script vuln -oN TestScanScript.txt")

# Print the scan results
print(scanner.all_hosts())
print(scanner[target_ip].hostname())
print(scanner[target_ip].state())
print(scanner[target_ip].all_protocols())
print(scanner[target_ip]['tcp'].keys())

# Save the scan results to a file
with open("TestScanScript.txt", "w") as f:
    f.write(scanner.csv())
