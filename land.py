import subprocess
import sys
import os
import time
from termcolor import colored
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt


# Check Python version
if sys.version_info.major < 3 or sys.version_info.minor < 9:
    print(colored('[!] Make sure you have Python 3.9+ installed, quitting.', 'yellow'))
    sys.exit(1)

# Define the command for theHarvester
domain = "10.10.11.211"
filename = "custom_results"
sources = "bing,anubis,brave,certspotter,crtsh"

# Additional options and customization
limit = "2000"
dns_server = "1.1.1.1"
takeover_check = True
screenshots_dir = "screenshots_dir"


command = [
    "theHarvester",
    "-d", domain,
    "-f", filename,
    "-b", sources,
    "-l", limit,
    "-vv",
    "-e", dns_server,
    "-t" if takeover_check else "",
    "--virtual-host",
    "--screenshot", screenshots_dir,
    "-s"
]

# Print a description of the script's purpose
print(colored("Running theHarvester to gather open source intelligence.", 'cyan'))

# Run the theHarvester command
print(colored(f"Executing theHarvester command with the following options:", 'cyan'))
print("  " + " ".join(command))  # Print the command as a string

start_time = time.time()
subprocess.run(command)
end_time = time.time()
# Print a completion message
print(colored("theHarvester script completed.", 'green'))

# Generate a report
report_data = [
    ["Domain", domain],
    ["Output File", filename],
    ["Sources", sources],
    ["Limit", limit],
    ["DNS Server", dns_server],
    ["Takeover Check", "Enabled" if takeover_check else "Disabled"],
    ["Screenshots Dir", screenshots_dir],
    ["Execution Time", f"{execution_time:.2f} seconds"]
]

report_table = tabulate(report_data, headers=["Parameter", "Value"], tablefmt="grid")
print(colored("\nReport:\n", 'cyan'))
print(report_table)


# Parse theHarvester output and gather source statistics
print(colored("\nParsing theHarvester output...\n", 'cyan'))
output_file_path = "/home/user1/Documents/scripts/scan-results.txt"  # Replace with the actual path
with open(output_file_path, 'r') as output_file:
    lines = output_file.readlines()

source_stats = {}
current_source = None
for line in lines:
    if line.startswith("[*] Searching"):
        current_source = line.split()[2][:-1]
    elif line.strip() == "":
        current_source = None
    elif current_source and line.startswith("[*]"):
        key, value = line[4:].strip().split(": ")
        source_stats.setdefault(current_source, {})[key] = value

# Process the parsed output and create a DataFrame
data = []  # List to store data
for line in lines:
    # Process each line and extract relevant information
    # Example: source, hosts = ...
    data.append((source, hosts))

# Create a DataFrame
df = pd.DataFrame(data, columns=['Source', 'Hosts'])

# Create a bar plot
plt.bar(df['Source'], df['Hosts'], color='skyblue')
plt.xlabel('Source')
plt.ylabel('Number of Hosts')
plt.title('Number of Hosts from Different Sources')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()

