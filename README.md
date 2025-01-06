# Port Scanner

A simple yet efficient Python-based port scanner that identifies open and closed ports on a given target. This tool is designed for educational purposes and to demonstrate basic network programming concepts.


---

## Features
- **Port Scanning**: Scans both individual ports and port ranges.
- **Hostname Resolution**: Resolves hostnames to IP addresses.
- **Graceful Interruptions**: Handles user interruptions (e.g., `Ctrl+C`) gracefully.
- **Error Handling**: Includes robust error handling for invalid inputs or unreachable targets.
- **Clear Output**: Provides clear and concise output for open and closed ports.

---

## Requirements
- **Python 3.6 or higher**
- Basic understanding of Python and networking concepts.

---

## Installation

1. **Clone the repository**:
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
2. **Verify Python Installation**:
Ensure you have Python 3 installed by running:
python3 --version

---

## Limitations
- **TCP Ports Only**: The script scans TCP ports only.
- **Single Target**: Scanning multiple targets simultaneously is not supported.
- **Performance**: High port ranges or slow networks may result in longer scan times.

---

## Disclaimer

This tool is for **educational purposes only**. Ensure you have proper authorization before scanning any system. Unauthorized scanning may violate laws and regulations in your region.
