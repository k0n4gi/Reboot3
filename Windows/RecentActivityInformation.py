import os
import datetime

def get_recent_items():
    # Recent Items 폴더의 경로를 가져옵니다.
    recent_folder = os.path.join(os.environ['USERPROFILE'], r'AppData\Roaming\Microsoft\Windows\Recent')
    recent_items = []

    # 폴더 내의 모든 파일과 폴더를 나열합니다.
    for item in os.listdir(recent_folder):
        item_path = os.path.join(recent_folder, item)
        item_stat = os.stat(item_path)
        
        # 파일의 마지막 액세스 시간을 가져옵니다.
        last_access_time = datetime.datetime.fromtimestamp(item_stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')
        recent_items.append(f"{item}: Last accessed at {last_access_time}")
        
    return recent_items

def save_to_txt(recent_info):
    # 현재 사용자의 바탕화면 경로를 가져옵니다.
    user_profile = os.environ['USERPROFILE']
    desktop_path = os.path.join(user_profile, 'Desktop')
    
    # 파일 이름에 현재 시간을 추가해 고유한 파일을 생성합니다.
    filename = os.path.join(desktop_path, f"recent_activity_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    # 최근 활동 정보를 .txt 파일에 저장합니다.
    with open(filename, 'w') as f:
        for info in recent_info:
            f.write(f"{info}\n")

if __name__ == "__main__":
    recent_info = get_recent_items()
    save_to_txt(recent_info)
