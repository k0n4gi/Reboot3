import os
import subprocess

def get_all_users_home_paths():
    # /etc/passwd 파일에서 사용자의 홈 디렉토리 경로들을 추출합니다.
    with open("/etc/passwd", "r") as f:
        lines = f.readlines()
        home_paths = []
        for line in lines:
            parts = line.split(":")
            if len(parts) > 5:
                home_path = parts[5]
                home_paths.append(home_path)
        return home_paths

def collect_trash_info_for_user(home_path):
    trash_info_path = os.path.join(home_path, ".local", "share", "Trash", "info")

    if not os.path.exists(trash_info_path):
        return []

    trashinfo_files = [f for f in os.listdir(trash_info_path) if f.endswith('.trashinfo')]
    
    collected_data = []
    for trashinfo_file in trashinfo_files:
        with open(os.path.join(trash_info_path, trashinfo_file), 'r') as file:
            collected_data.append(file.read())
    print(f"Found {len(trashinfo_files)} .trashinfo files in {trash_info_path}")

    return collected_data

def save_to_txt(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(item + "\n\n")

def get_current_user():
    result = subprocess.run(["whoami"], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()

if __name__ == "__main__":
    username = get_current_user()

    if username == "root":
        while True:
            username = input("사용자가 root로 실행되었습니다. 히스토리를 가져올 대상의 사용자를 입력 후 엔터 :")
            ask = input(f"사용자가 {username}이 맞습니까 y/n ")
            if ask == 'y' or ask == "Y":
                break
    
    # 입력받은 사용자의 홈 디렉토리 경로
    home_path = os.path.join("/home", username)
    
    all_data = collect_trash_info_for_user(home_path)
    save_to_txt(all_data, "trash_forensics.txt")
