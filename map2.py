import subprocess
import sys

# Check Python version
if sys.version_info.major < 3 or sys.version_info.minor < 9:
    print('\033[93m[!] Make sure you have Python 3.9+ installed, quitting.\n\n \033[0m')
    sys.exit(1)

# Define the command for theHarvester
domain = "https://enginueeur.com"
filename = "custom_results"
sources = "bing,anubis,brave,certspotter,crtsh"

# Construct the command with options and arguments
command = [
    "theHarvester",
    "-d", domain,
    "-f", filename,
    "-b", sources,
    "-l", "1000",
    "-vv",  # Increase verbosity
    "-e", "8.8.8.8",
    "-t",
    "--virtual-host",
    "--screenshot", "screenshots_dir",
    "-s"
]

# Print a description of the script's purpose
print("Running theHarvester to gather open source intelligence.")

# Run the command and provide a description
print("Executing theHarvester command with the following options:")
print(" ".join(command))  # Print the command as a string
subprocess.run(command)

# Print a message to indicate completion
print("theHarvester script completed.")
