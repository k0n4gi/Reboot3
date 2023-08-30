import socket
import os

def get_open_ports():
    open_ports = []
    
    # 확인하고자 하는 포트 범위 지정 (예: 1부터 65535까지)
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 연결 시도 시간 초과 설정
        
        result = sock.connect_ex(('localhost', port))
        if result == 0:
            open_ports.append(port)
        
        sock.close()

    return open_ports

def get_ip_address():
    # 호스트 이름을 가져옴
    hostname = socket.gethostname()
    
    # 호스트 이름을 IP 주소로 변환
    ip_address = socket.gethostbyname(hostname)
    
    return ip_address

def get_arp_address():
    # 셸 명령어를 사용하여 ARP 테이블 조회
    command = "arp -a"
    result = os.popen(command).read()
    
    # ARP 주소 추출
    arp_address = []
    lines = result.splitlines()
    for line in lines:
        if "at" in line:
            parts = line.split()
            arp_address.append(parts[3])
    
    return arp_address

if __name__ == "__main__":
    open_ports = get_open_ports()
    ip_address = get_ip_address()
    arp_address = get_arp_address()

    with open('port_ip_arp.txt', 'w') as file:
        file.write("열린 포트:\n")
        for port in open_ports:
            file.write(str(port) + '\n')

        file.write(f"\n현재 컴퓨터의 IP 주소: {ip_address}\n\n")
        
        file.write("현재 컴퓨터의 ARP 주소:\n")
        for address in arp_address:
            file.write(address + '\n')

    print("결과가 'port_ip_arp.txt' 파일에 저장되었습니다.")
