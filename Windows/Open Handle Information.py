import psutil
import os
import datetime

def get_process_handle_info():
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        processes.append(proc.info)

    return processes

def save_to_txt(processes):
    # 현재 사용자의 바탕화면 경로를 구합니다.
    user_profile = os.environ['USERPROFILE']
    desktop_path = os.path.join(user_profile, 'Desktop')
    
    # 파일 이름에 현재 시간을 추가해 고유한 파일을 생성합니다.
    filename = os.path.join(desktop_path, f"handle_info_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    # 핸들 정보를 .txt 파일에 저장합니다.
    with open(filename, 'w') as f:
        for proc in processes:
            f.write(f"PID: {proc['pid']}, Name: {proc['name']}\n")
            if proc['open_files']:
                for open_file in proc['open_files']:
                    f.write(f"\t{open_file}\n")

if __name__ == "__main__":
    processes = get_process_handle_info()
    save_to_txt(processes)
