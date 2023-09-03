import subprocess
import os
import datetime

def get_arp_info():
    try:
        # 'arp -a' 명령을 실행하고 결과를 반환받습니다.
        arp_output = subprocess.check_output("arp -a", shell=True, stderr=subprocess.STDOUT, text=True)
        return arp_output
    except subprocess.CalledProcessError as e:
        return f"An error occurred while trying to fetch ARP info: {str(e)}"

def save_to_txt(arp_info):
    # 현재 사용자의 바탕화면 경로를 가져옵니다.
    user_profile = os.environ['USERPROFILE']
    desktop_path = os.path.join(user_profile, 'Desktop')
    
    # 파일 이름에 현재 시간을 추가하여 고유하게 만듭니다.
    filename = os.path.join(desktop_path, f"arp_info_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    # ARP 정보를 .txt 파일에 저장합니다.
    with open(filename, 'w') as f:
        f.write(arp_info)

if __name__ == "__main__":
    arp_info = get_arp_info()
    save_to_txt(arp_info)
