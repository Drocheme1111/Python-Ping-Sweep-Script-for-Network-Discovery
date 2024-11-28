# Python-Ping-Sweep-Script-for-Network-Discovery
This repository contains a simple Python script for network discovery using the subprocess module.
The script allows users to check the availability of a specific host by pinging its IP address. It provides a quick and efficient way to determine whether a host is alive or down.
Features:
User Input: Accepts an IP address from the user.
Ping Execution: Uses the subprocess.run function to execute a ping command.
Output Suppression: Suppresses standard output (stdout) and error output (stderr) for cleaner execution.
Status Check: Evaluates the return code from the ping command to determine the host's status:
Host is alive: If the ping command is successful.
Host is down: If the ping command fails.
Requirements:
Python 3.x
The script relies on the ping command, so ensure it is available on your operating system.
Usage:
Clone this repository or copy the script to your local machine.
Run the script in your Python environment.
Enter an IP address when prompted.
View the result indicating whether the host is reachable.
This script is ideal for beginners in Python and cybersecurity who are learning about network discovery techniques and automation.







