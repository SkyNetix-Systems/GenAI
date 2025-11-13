import subprocess  # Import subprocess for executing shell commands

with open('hosts.txt') as f:
    ip_addresses = f.read().splitlines()  # Read all IP addresses from file and remove newline characters

    for ip in ip_addresses:
        try:
            # Run a single ping command for the current IP and capture the output
            output = subprocess.check_output(f'ping -c 1 {ip}'.split())

            # Decode and print the ping response
            print(output.decode('utf-8'))
        except Exception as e:
            # Handle errors if the host is unreachable or the command fails
            print(f'Host {ip} is down! ==> {e}')

        # Print a separator for better readability
        print('#' * 50)

