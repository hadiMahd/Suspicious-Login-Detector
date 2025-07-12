import re
from collections import defaultdict

# Path to the log file
LOG_FILE = "sample_auth.log"  # change to "/var/log/auth.log" on real system

# Dictionary to track failed logins per IP
failed_logins = defaultdict(int)

# Pattern to match failed SSH login attempts
pattern = re.compile(r'Failed password.*from (\d+\.\d+\.\d+\.\d+)')

with open(LOG_FILE, 'r') as file:
    for line in file:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            failed_logins[ip] += 1

# Show IPs with 3 or more failed attempts
print("Suspicious IPs with multiple failed login attempts:")
for ip, count in failed_logins.items():
    if count >= 3:
        print(f" - {ip}: {count} failed attempts")
