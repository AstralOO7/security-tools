import socket

def scan_port(ip,port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip,port))
        s.close()
        return result == 0
    except:
        return False
    
def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "unknown"    
    
def scan_ports(ip, start, end):
    print(f"\n[*] Scanning {ip} from port {start} to {end}\n")
    open_ports = []
    for port in range(start, end + 1):
        if scan_port(ip, port):
            service = get_service(port)
            print(f"[+] Port {port} is OPEN — {service}")
            open_ports.append(port)
        else:
            print(f"[-] Port {port} closed")
    print(f"\n[*] Scan complete. {len(open_ports)} open ports found.")

ip = input("Enter target IP: ")
start = int(input("Enter start port: "))
end = int(input("Enter end port: "))

scan_ports(ip, start, end)