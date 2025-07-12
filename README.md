# Suspicious-Login-Detector
A Python script that scans Linux auth logs for brute-force SSH login attempts.
## Features

- Detects 5+ failed login attempts within a configurable time window.
- Outputs alerts to console and file.
- Supports whitelisting trusted IPs.
- Accepts command-line arguments for flexibility.

## How to Run
Change logs file path in python file first, then:
```bash
python3 detector.py
```
sample output: "Suspicious IPs with multiple failed login attempts:
 - 192.168.1.101: 4 failed attempts
"
