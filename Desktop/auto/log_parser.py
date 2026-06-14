import re
from collections import Counter

def parse_log(filename, threshold=3):
    print(f"\n[*] Parsing log file: {filename}\n")
    
    ip_counts = Counter()
    
    with open(filename, "r") as f:
        for line in f:
            match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if match:
                ip = match.group()
                ip_counts[ip] += 1
    
    print("[*] Request count per IP:")
    for ip, count in ip_counts.most_common():
        print(f"    {ip} — {count} requests")
    
    print(f"\n[!] Suspicious IPs (more than {threshold} requests):")
    found = False
    for ip, count in ip_counts.items():
        if count > threshold:
            print(f"    [ALERT] {ip} — {count} requests")
            found = True
    
    if not found:
        print("    None found.")

parse_log("sample.log")
