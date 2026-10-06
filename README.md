*Network Triage Tool

A Python-based network troubleshooting and basic security assessment tool.
# Project Overview
Network Triage Tool helps security analysts and beginners perform basic network diagnostics from the command line.
The tool can:
-Display local hostname and IP address
-Perform DNS resolution
-Test network connectivity using Ping
-Check common TCP ports
-Identify open common services
-Provide basic security observations
# Features
1. Network Information
Displays:
Hostname
Local IP address
2. DNS Lookup
Resolves a domain name to an IP address and retrieves the resolved hostname.
3. Ping Test
Checks whether the target is reachable.
4. Common Port Scan
Checks commonly used ports:
Port Service
21 FTP
22 SSH
23 Telnet
25 SMTP
53 DNS
80 HTTP
443 HTTPS
3389 RDP
5. Security Assessment
Provides basic observations when potentially sensitive or insecure services are detected.

**Technologies Used
-Python
-Socket Programming
-Subprocess
-Network Troubleshooting
-Basic Security Analysis
**Requirements
-Python 3.x
-Windows, Linux, or macOS

No external Python libraries are required.
**How to Run
Open a terminal inside the project folder and run:
     python network_triage.py

Enter a domain or IP address 
when prompted.

Example:
google.com

Example Workflow

NETWORK TRIAGE TOOL

[Network Information]
Hostname: YOUR-COMPUTER
Local IP: 192.168.x.x

[1] DNS Lookup
Domain: google.com
IP Address: xxx.xxx.xxx.xxx
[2] Ping Test
Status: Reachable
[3] Common Port Scan
Port 80 (HTTP): OPEN
Port 443 (HTTPS): OPEN
[4] Security Assessment
Open ports detected: 2

Triage completed successfully.

# Security and Ethical Use

This tool is intended for educational purposes, troubleshooting, and authorized security testing.

Only scan systems and networks that you own or have explicit permission to test.

# Learning Objectives
This project demonstrates practical understanding of:
- Python networking
- DNS resolution
- TCP connections
- Network troubleshooting
- Basic port scanning
- Security assessment
- Command-line security tools
# Future Improvements
Possible future improvements include:
- Detailed service detection
- Timeout configuration
- Logging results to a file
- JSON report generation
- Better error handling
- Network interface detection
- More advanced security checks
# Author
Computer Science Student | Cybersecurity & Security Analysis
GitHub Portfolio Project