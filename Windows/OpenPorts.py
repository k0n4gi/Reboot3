import os
import psutil

def get_open_ports():
    open_ports = []
    for conn in psutil.net_connections(kind='inet'):
        laddr, raddr, status, pid = conn.laddr, conn.raddr, conn.status, conn.pid
        if raddr:
            open_ports.append(f"{laddr} <--> {raddr} {status} {pid}")
        else:
            open_ports.append(f"{laddr} {status} {pid}")
    return open_ports

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
    file_path = os.path.join(desktop_path, "open_ports.txt")
    
    open_ports = get_open_ports()

    with open(file_path, 'w') as f:
        for port in open_ports:
            f.write(f"{port}\n")
    
    print(f"Open port information has been saved to {file_path}")
