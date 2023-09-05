import os
import getpass

def collect_trash_info_for_user(home_path):
    # 휴지통 정보가 저장되어 있는 경로를 생성합니다.
    trash_info_path = os.path.join(home_path, ".local", "share", "Trash", "info")

    # 해당 경로가 존재하는지 확인합니다.
    if not os.path.exists(trash_info_path):
        print(f"{trash_info_path}에 휴지통 정보 디렉토리가 없습니다.")
        return []

    # .trashinfo 파일을 찾아 리스트에 추가합니다.
    trashinfo_files = [f for f in os.listdir(trash_info_path) if f.endswith('.trashinfo')]
    
    collected_data = []
    for trashinfo_file in trashinfo_files:
        # 각 .trashinfo 파일을 읽어 정보를 수집합니다.
        with open(os.path.join(trash_info_path, trashinfo_file), 'r') as file:
            collected_data.append(file.read())
    print(f"{trash_info_path}에 {len(trashinfo_files)}개의 .trashinfo 파일을 찾았습니다.")

    return collected_data

def save_to_txt(data, filename):
    # 수집한 데이터를 텍스트 파일에 저장합니다.
    with open(filename, 'w') as file:
        for item in data:
            file.write(item + "\n\n")
    print(f"{filename}에 데이터를 저장했습니다.")

if __name__ == "__main__":
    # 홈 디렉토리 경로를 직접 설정합니다.
    username = getpass.getuser()  # 현재 실행 사용자의 이름을 가져옴
    home_path = os.path.join("/home", username)  # 홈 디렉토리 경로 설정
    
    # 휴지통 정보를 수집합니다.
    all_data = collect_trash_info_for_user(home_path)
    
    if all_data:
        # 수집한 데이터가 있다면 텍스트 파일에 저장합니다.
        save_to_txt(all_data, "trash_forensics.txt")
    else:
        print("휴지통 정보가 없습니다.")
