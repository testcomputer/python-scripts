import subprocess

domain = "10.10.10.211"
filename = "custom_results"
sources = "bing,anubis,brave,certspotter,crtsh"

command = [
    "theHarvester",
    "-d", domain,
    "-f", filename,
    "-b", sources,
    "-l", "1000",
    "-v", "-v",
    "-e", "8.8.8.8",
    "-t",
    "--virtual-host",
    "--screenshot", "screenshots_dir",
    "-s"
]

subprocess.run(command)
