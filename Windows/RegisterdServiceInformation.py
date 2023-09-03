import subprocess
import os
import datetime

def get_service_info():
    try:
        # 'sc query' 명령을 실행하여 서비스 정보를 가져옵니다.
        output = subprocess.check_output("sc query", shell=True, text=True, stderr=subprocess.STDOUT)
        return output
    except subprocess.CalledProcessError as e:
        return f"An error occurred while trying to fetch service info: {str(e)}"

def save_to_txt(service_info):
    # 현재 사용자의 바탕화면 경로를 가져옵니다.
    user_profile = os.environ['USERPROFILE']
    desktop_path = os.path.join(user_profile, 'Desktop')
    
    # 파일 이름에 현재 시간을 추가해 고유한 파일을 생성합니다.
    filename = os.path.join(desktop_path, f"service_info_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    # 서비스 정보를 .txt 파일에 저장합니다.
    with open(filename, 'w') as f:
        f.write(service_info)

if __name__ == "__main__":
    service_info = get_service_info()
    save_to_txt(service_info)
