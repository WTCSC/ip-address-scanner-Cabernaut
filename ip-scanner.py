import argparse
import ipaddress
import subprocess
import platform
import time

# Function to ping a host and return its status and response time
def ping_host(ip):
    """Pings a host and returns its status and response time."""
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    try:
        start_time = time.time()
        result = subprocess.run(["ping", param, ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        end_time = time.time()
        
        if result.returncode == 0:
            return "UP", round((end_time - start_time) * 1000)  # Convert to milliseconds
        else:
            return "DOWN", "No response"
    except Exception as e:
        return "ERROR", str(e)

# Function to scan the given network range and report active hosts
def scan_network(cidr):
    """Scans the given network range and reports active hosts."""
    network = ipaddress.ip_network(cidr, strict=False)
    
    print(f"Scanning network {cidr}...\n")
    up_count = 0
    down_count = 0
    error_count = 0
    
    for ip in network.hosts():  # Iterate over all valid hosts in the network
        status, response = ping_host(str(ip))
        print(f"{ip} - {status} ({response}ms)" if status == "UP" else f"{ip} - {status} ({response})")
        
        if status == "UP":
            up_count += 1
        elif status == "DOWN":
            down_count += 1
        else:
            error_count += 1
    
    # Display scan summary
    print(f"\nScan complete. Found {up_count} active hosts, {down_count} down, {error_count} errors.")

# Main execution block to parse arguments and start scanning
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple IP Scanner")
    parser.add_argument("cidr", help="CIDR notation (e.g., 192.168.1.0/24)")
    args = parser.parse_args()
    scan_network(args.cidr)
