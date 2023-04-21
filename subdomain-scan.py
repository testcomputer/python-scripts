import subprocess

# Replace example.com with the target domain
target_domain = "example.com"

# Run the sublist3r tool and capture its output
sublist3r_output = subprocess.check_output(["sublist3r", "-d", target_domain])

# Decode the output from bytes to a string
sublist3r_output = sublist3r_output.decode()

# Print the subdomains
print("Subdomains for", target_domain)
print(sublist3r_output)
