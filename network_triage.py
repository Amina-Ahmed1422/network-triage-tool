import socket 
import subprocess 
import platform
# ==========================================
# Network Triage Tool
# ==========================================

print("=" * 50) 
print("          NETWORK TRIAGE TOOL") 
print("=" * 50) 
print("Network diagnostics and basic security assessment") 
print("=" * 50)

# ==========================================
# Network Information
# ==========================================

print("\n[Network Information]")

hostname = socket.gethostname()

try: 
    local_ip = socket.gethostbyname(hostname) 
except socket.gaierror: 
    local_ip = "Unable to determine"

print(f"Hostname: {hostname}") 
print(f"Local IP: {local_ip}")

# ==========================================
# Target Input
# ==========================================

target = input("\nEnter IP address or domain: ")

# ==========================================
# DNS Lookup
# ==========================================

print("\n[1] DNS Lookup")

try: 
    ip_address = socket.gethostbyname(target) 
    resolved_hostname = socket.gethostbyaddr(ip_address)[0]

print(f"Domain: {target}")
print(f"IP Address: {ip_address}")
print(f"Resolved Hostname: {resolved_hostname}")

except socket.gaierror: 
    print("DNS lookup failed.") 
    ip_address = None

# ==========================================
# Ping Test
# ==========================================
print("\n[2] Ping Test")

if ip_address:

    if platform.system() == "Windows":
    command = ["ping", "-n", "1", target]
else:
    command = ["ping", "-c", "1", target]

result = subprocess.run(
    command,
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Status: Reachable")
else:
    print("Status: Unreachable")
else: print("Ping skipped because DNS resolution failed.")
# ==========================================
# Common Port Scan
# ==========================================
print("\n[3] Common Port Scan")

common_ports = {
     21: "FTP", 
     22: "SSH", 
     23: "Telnet", 
     25: "SMTP", 
     53: "DNS", 
     80: "HTTP", 
     443: "HTTPS", 
     3389: "RDP" 
}     
open_ports = []
if ip_address:
    for port, service in common_ports.items():

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.settimeout(1)

    result = sock.connect_ex(
        (ip_address, port)
    )

    if result == 0:
        print(f"Port {port} ({service}): OPEN")
        open_ports.append((port, service))
    else:
        print(f"Port {port} ({service}): CLOSED")

    sock.close()
else: print("Port scan skipped because DNS resolution failed.")
# ==========================================
# Security Assessment
# ==========================================
print("\n[4] Security Assessment")
if ip_address:
    if open_ports:
        print(f"Open ports detected: {len(open_ports)}")

    for port, service in open_ports:
        print(f"- {port}/{service}")

        if port == 23:
            print(
                "  WARNING: Telnet is insecure "
                "and should generally be avoided."
            )

        elif port == 21:
            print(
                "  WARNING: FTP transmits data "
                "without encryption by default."
            )

        elif port == 3389:
            print(
                "  INFO: RDP should be properly secured "
                "and restricted."
            )

else:
    print("No common open ports detected.")
else: print("Security assessment skipped.")
# ==========================================
# Completion
# ==========================================
print("\n" + "=" * 50) 
print("Triage completed successfully.") 
print("=" * 50)