import socket
import psutil
import os
import datetime

def get_ip_info():
    ip_info = {}
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    ip_info["Hostname"] = hostname
    ip_info["Local IP"] = local_ip
    
    interfaces = psutil.net_if_addrs()
    for interface, addrs in interfaces.items():
        ip_info[interface] = []
        for addr in addrs:
            ip_info[interface].append(str(addr))
            
    return ip_info

def save_to_txt(ip_info):
    user_profile = os.environ['USERPROFILE']
    desktop_path = os.path.join(user_profile, 'Desktop')
    filename = os.path.join(desktop_path, f"ip_info_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    with open(filename, 'w') as f:
        for key, value in ip_info.items():
            f.write(f"{key}: {value}\n")

if __name__ == "__main__":
    ip_info = get_ip_info()
    save_to_txt(ip_info)
