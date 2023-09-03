import subprocess
import os
import datetime

def get_netbios_info():
    try:
        # 'nbtstat -n' 명령을 실행하고 그 결과를 반환합니다.
        netbios_output = subprocess.check_output("nbtstat -n", shell=True, stderr=subprocess.STDOUT, text=True)
        return netbios_output
    except subprocess.CalledProcessError as e:
        return f"An error occurred while trying to fetch NetBIOS info: {str(e)}"

def save_to_txt(netbios_info):
    # 현재 사용자의 바탕화면 경로를 구합니다.
    user_profile = os.environ['USERPROFILE']
    desktop_path = os.path.join(user_profile, 'Desktop')
    
    # 파일 이름에 현재 시간을 추가해 고유한 파일을 생성합니다.
    filename = os.path.join(desktop_path, f"netbios_info_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    # NetBIOS 정보를 .txt 파일에 저장합니다.
    with open(filename, 'w') as f:
        f.write(netbios_info)

if __name__ == "__main__":
    netbios_info = get_netbios_info()
    save_to_txt(netbios_info)
