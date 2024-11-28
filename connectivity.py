import subprocess

# Get the IP address from the user
ip = input("Enter your IP address: ")

# Run the ping command and suppress stdout and stderr
response = subprocess.run(
    ["ping", "/n", "1", ip], 
    stdout=subprocess.DEVNULL, 
    stderr=subprocess.DEVNULL
)

# Check the return code to determine the host status
if response.returncode == 0:
    print("Host is alive")
else:
    print("Host is down")

