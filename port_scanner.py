import socket
import sys
from datetime import datetime

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Closed")
    except socket.error as e:
        print(f"Couldn't connect to server: {e}")

def port_scanner(target, ports):
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Scanning target: {target_ip}")
        print(f"Scanning started at: {datetime.now()}")
        
        for port in ports:
            scan_port(target_ip, port)
            
        print(f"Scanning finished at: {datetime.now()}")
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit()

def parse_ports(ports_input):
    ports = []
    for item in ports_input:
        if '-' in item:
            start, end = map(int, item.split('-'))
            ports.extend(range(start, end + 1))
        else:
            ports.append(int(item))
    return ports

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python port_scanner.py <target> <ports>")
        print("Ports can be individual ports (e.g., 80 443 8080) or ranges (e.g., 1-1024)")
        sys.exit()
    
    target = sys.argv[1]
    ports_input = sys.argv[2:]
    
    try:
        ports_to_scan = parse_ports(ports_input)
    except ValueError:
        print("Invalid port format. Please provide valid port numbers or ranges.")
        sys.exit()
    
    port_scanner(target, ports_to_scan)