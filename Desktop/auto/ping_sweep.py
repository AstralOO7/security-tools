import os
import sys

def ping_host(ip):
    response = os.system("ping -c 1 -W 1 " + ip + " > /dev/null 2>&1")
    return response == 0

def scan_network(base_ip,start,end):
     print(f"\n[*] Scanning {base_ip}.{start} to {base_ip}.{end}\n")
     alive = []
     for i in range(start,end+1):
          ip = f"{base_ip}.{i}"
          if ping_host(ip):
               alive.append(ip)
          with open("results.txt", "w") as f:
            for ip in alive:
              f.write(ip + "\n")
               
     print(f"\n[*] Scan complete. {len(alive)} hosts found alive.")   

base_ip = input("Enter network base (e.g. 192.168.1): ")
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

scan_network(base_ip, start, end)