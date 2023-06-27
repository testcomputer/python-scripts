import subprocess

target_ip = "{target ip}"

# Scan top 100 ports
# Execute nmap command to perform a scan for open ports
port_scan_command = f"nmap -p 1-100 {target_ip}"
port_scan_process = subprocess.Popen(port_scan_command.split(), stdout=subprocess.PIPE)
port_scan_output, port_scan_error = port_scan_process.communicate()

# Execute nmap command to perform a vulnerability scan
vuln_scan_command = f"nmap -p 1-100 --script vuln {target_ip}"
vuln_scan_process = subprocess.Popen(vuln_scan_command.split(), stdout=subprocess.PIPE)
vuln_scan_output, vuln_scan_error = vuln_scan_process.communicate()

# Process the port scan results
if port_scan_output:
    # Extract relevant information from the port scan output
    # Perform analysis, extract open ports, or identify active hosts, etc.
    # You can use Python's regular expressions, string manipulation, or other methods

    # Output the port scan results
    port_scan_results_file = "port_scan_results.txt"
    with open(port_scan_results_file, "w") as f:
        f.write(port_scan_output.decode())
    print(f"Port scan results saved to {port_scan_results_file}")
else:
    print("An error occurred during the port scan.")

# Process the vulnerability scan results
if vuln_scan_output:
    # Extract relevant information from the vulnerability scan output
    # Perform analysis, extract vulnerabilities, or identify vulnerable hosts, etc.
    # You can use Python's regular expressions, string manipulation, or other methods

    # Output the vulnerability scan results
    vuln_scan_results_file = "vuln_scan_results.txt"
    with open(vuln_scan_results_file, "w") as f:
        f.write(vuln_scan_output.decode())
    print(f"Vulnerability scan results saved to {vuln_scan_results_file}")
else:
    print("An error occurred during the vulnerability scan.")
