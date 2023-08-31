#sudo 사용
#Mac os 시스템 정보(운영체제 버전, 시스템 아키텍처, 사용자 이름, 호스트 이름, 네트워크 정보, 디스크 사용량, 로그인된 사용자)
import os
import platform
import socket
import subprocess

def get_os_version():
    return platform.mac_ver()[0]

def get_architecture():
    return platform.architecture()[0]

def get_username():
    return os.getlogin()

def get_hostname():
    return socket.gethostname()

def get_network_info():
    return subprocess.check_output(['ifconfig']).decode()

def get_disk_usage():
    return subprocess.check_output(['df', '-h']).decode()

def get_logged_in_users():
    return subprocess.check_output(['who']).decode()

def main():
    with open('system_information.txt', 'w') as file:
        file.write("OS Version: " + get_os_version() + '\n')
        file.write("Architecture: " + get_architecture() + '\n')
        file.write("Username: " + get_username() + '\n')
        file.write("Hostname: " + get_hostname() + '\n\n')
        file.write("Network Info:\n" + get_network_info() + '\n')
        file.write("Disk Usage:\n" + get_disk_usage() + '\n')
        file.write("Logged-in Users:\n" + get_logged_in_users() + '\n')

if __name__ == '__main__':
    main()
