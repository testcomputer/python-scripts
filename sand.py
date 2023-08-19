import subprocess
import time
from termcolor import colored
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt

# Ensure Python version compatibility
required_python_version = (3, 9)
if sys.version_info < required_python_version:
    print(colored(f'[!] Please install Python {required_python_version[0]}.{required_python_version[1]} or higher. Exiting.', 'yellow'))
    sys.exit(1)

# Define theHarvester command parameters
domain = "https://enginueeur.com"
filename = "custom_results"
sources = "bing,anubis,brave,certspotter,crtsh"
limit = "2000"
dns_server = "1.1.1.1"
takeover_check = True
screenshots_dir = "screenshots_dir"

# Construct theHarvester command
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

# Print the script's objective
print(colored("Running theHarvester to gather open-source intelligence.", 'cyan'))

# Execute the theHarvester command
print(colored("Executing theHarvester command with the following options:", 'cyan'))
print("  " + " ".join(command))  # Display the command string

start_time = time.time()
subprocess.run(command)
end_time = time.time()

# Display completion message
print(colored("theHarvester script completed.", 'green'))

# Generate a report
execution_time = end_time - start_time
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

# Parse theHarvester output and extract source statistics
print(colored("\nParsing theHarvester output...\n", 'cyan'))
with open(filename + '.txt', 'r') as output_file:
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

# Create a pandas DataFrame from the source statistics
df = pd.DataFrame(source_stats).T
df.reset_index(inplace=True)
df.rename(columns={'index': 'Source'}, inplace=True)

# Generate a bar graph depicting subdomains per source
plt.figure(figsize=(10, 6))
plt.bar(df['Source'], df['Hosts'], color='skyblue')
plt.title('Number of Subdomains from Each Source')
plt.xlabel('Source')
plt.ylabel('Number of Subdomains')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the graph as an image
graph_filename = 'subdomains_by_source.png'
plt.savefig(graph_filename)
print(colored(f"Bar graph saved as: {graph_filename}\n", 'green'))

# Display the graph
plt.show()

In this improved version, I added a required Python version check, revised comments for clarity, and adjusted code organization to enhance readability. Additionally, I removed unnecessary imports and kept the code structure consistent for better maintenance.
