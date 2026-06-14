import re
from collections import Counter

def analyze_log(filename, request_threshold=3, failed_threshold=3):
    print(f"\n[*] Analyzing log file: {filename}\n")
    
    ip_counts = Counter()
    failed_logins = Counter()
    
    with open(filename, "r") as f:
        for line in f:
            match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if not match:
                continue
            ip = match.group()
            ip_counts[ip] += 1
            
            if line.strip().endswith("401"):
                failed_logins[ip] += 1
    
    print("[*] Request count per IP:")
    for ip, count in ip_counts.most_common():
        print(f"    {ip} — {count} requests")
    
    print(f"\n[!] High traffic IPs (more than {request_threshold} requests):")
    found = False
    for ip, count in ip_counts.items():
        if count > request_threshold:
            print(f"    [ALERT] {ip} — {count} requests")
            found = True
    if not found:
        print("    None found.")
    
    print(f"\n[!] Possible brute force (more than {failed_threshold} failed logins):")
    found = False
    for ip, count in failed_logins.items():
        if count >= failed_threshold:
            print(f"    [CRITICAL] {ip} — {count} failed login attempts")
            found = True
    if not found:
        print("    None found.")

analyze_log("sample.log")