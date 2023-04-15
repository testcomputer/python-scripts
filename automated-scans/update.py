# Tested and passed

import subprocess

# Run the software update command and capture the output
output = subprocess.check_output(["softwareupdate", "-l"])

# Check if any updates are available
if "No new software available." in output.decode("utf-8"):
	print("Your macOS is up to date!")
else:
	print("Updates are available!")


# Run using ‘python3 update.py’

# Only checks for updates, doesn’t run the actual update

# Script is for: MacOS
