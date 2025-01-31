Overview

This Python script scans a network range specified in CIDR notation and reports the status of each host. It uses the ping command to check if hosts are up or down and provides a summary of the scan results.

Features

Takes a CIDR notation input (e.g., 192.168.1.0/24)

Calculates the network range based on the subnet mask

Iterates over all valid host addresses in the range

Reports which IP addresses successfully respond to ping requests

Displays response time in milliseconds

Provides a summary of active, down, and error hosts

Requirements

Python 3.x

ipaddress module (built-in with Python 3.3+)

Installation

No additional dependencies are required beyond Python. Simply clone this repository and run the script.

Usage

To scan a network, use the following command:

python ip_scanner.py 192.168.1.0/24

Example output:

Scanning network 192.168.1.0/24...

192.168.1.1   - UP   (2ms)
192.168.1.2   - DOWN (No response)
192.168.1.3   - UP   (5ms)
192.168.1.4   - UP   (3ms)
192.168.1.5   - ERROR (Connection timeout)
...

Scan complete. Found 3 active hosts, 1 down, 1 error.
