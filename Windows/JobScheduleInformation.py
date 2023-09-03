import subprocess
import os
import datetime

def get_task_scheduler_info():
    try:
        # 'schtasks' 명령을 실행하고 그 결과를 반환합니다.
        output = subprocess.check_output("schtasks /query /fo LIST", shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"An error occurred while trying to fetch task scheduler info: {str(e)}"

def save_to_txt(task_info):
    # 현재 사용자의 바탕화면 경로를 구합니다.
    user_profile = os.environ['USERPROFILE']
    desktop_path = os.path.join(user_profile, 'Desktop')
    
    # 파일 이름에 현재 시간을 추가해 고유한 파일을 생성합니다.
    filename = os.path.join(desktop_path, f"task_scheduler_info_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    # 작업 스케줄러 정보를 .txt 파일에 저장합니다.
    with open(filename, 'w') as f:
        f.write(task_info)

if __name__ == "__main__":
    task_info = get_task_scheduler_info()
    save_to_txt(task_info)
