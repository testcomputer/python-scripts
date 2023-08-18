import subprocess
import sys
import os
import time
from termcolor import colored
from tabulate import tabulate

# Check Python version
if sys.version_info.major < 3 or sys.version_info.minor < 9:
    print(colored('[!] Make sure you have Python 3.9+ installed, quitting.', 'yellow'))
    sys.exit(1)

# Define the command for theHarvester
domain = "https://enginueeur.com"
filename = "custom_results"
sources = "bing,anubis,brave,certspotter,crtsh"

# Additional options and customization
limit = "2000"
dns_server = "1.1.1.1"
takeover_check = True
screenshots_dir = "screenshots_dir"

# Construct the command with options and arguments
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

# Display execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.2f} seconds")

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

# Create visualizations or perform further analysis if desired
# For example, you can use libraries like matplotlib to create graphs
# or pandas to manipulate and analyze the gathered data.
