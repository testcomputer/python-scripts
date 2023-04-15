# Requires 'sudo' to run

# For example, 'sudo python3 bluetooth.py'

import subprocess

# execute the command to enable Bluetooth
subprocess.run(["defaults", "write", "/Library/Preferences/com.apple.Bluetooth", "ControllerPowerState", "1"])

# check the status of Bluetooth
status = subprocess.check_output(["defaults", "read", "/Library/Preferences/com.apple.Bluetooth", "ControllerPowerState"]).decode().strip()

if status == "1":
    print("Bluetooth is now turned on.")
else:
    print("There was an error turning on Bluetooth.")
