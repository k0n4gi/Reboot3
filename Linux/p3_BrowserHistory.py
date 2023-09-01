import os
import sqlite3
import shutil
import sys
import psutil

def is_browser_running(browser_name):
    for process in psutil.process_iter():
        try:
            if browser_name in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if is_browser_running('firefox'):
    print("Firefox가 실행 중입니다. 브라우저를 닫고 다시 시도하세요.")

# 환경에 따른 경로 설정
if os.name == 'nt':  # Windows 환경
    base_path = "C:/Users"
else:  # WSL 환경
    base_path = "/mnt/c/Users"

# Windows 사용자 이름
windows_username = "user"  # 여기에 실제 Windows 사용자 이름을 입력하세요

# Firefox 프로필 경로
firefox_path = os.path.join(base_path, windows_username, "AppData", "Roaming", "Mozilla", "Firefox")

# Chrome 프로필 경로
chrome_path = os.path.join(base_path, windows_username, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "History")

# SQLite 데이터를 추출하는 함수
def extract_sqlite_data(db_path, query):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(f"Error reading {db_path}: {str(e)}")
        return []

if not os.access(firefox_path, os.R_OK):
    print("Firefox 경로에 접근할 수 없습니다. 권한을 확인하세요.")

# 출력을 파일에 저장할 경로
output_file_path = "linuxweboutput.txt"

# 기존 출력 스트림을 백업하고 파일로 변경
original_stdout = sys.stdout
with open(output_file_path, "w") as f:
    sys.stdout = f

    # Firefox 인터넷 기록을 추출합니다.
    for profile_directory in os.listdir(firefox_path):
        if profile_directory.endswith('.default-release'):
            places_db = os.path.join(firefox_path, profile_directory, 'places.sqlite')
            if os.path.exists(places_db):
                temp_copy = os.path.join("/tmp", "temp_places.sqlite")
                shutil.copy(places_db, temp_copy)
                query = "SELECT url, title, last_visit_date FROM moz_places"
                records = extract_sqlite_data(temp_copy, query)
                os.remove(temp_copy)
                for record in records:
                    print(record)

    # Chrome 인터넷 기록을 추출합니다.
    if os.path.exists(chrome_path):
        temp_copy = os.path.join("/tmp", "temp_history.sqlite")
        shutil.copy(chrome_path, temp_copy)
        query = "SELECT url, title, last_visit_time FROM urls"
        records = extract_sqlite_data(temp_copy, query)
        os.remove(temp_copy)
        for record in records:
            print(record)

# 기존 출력 스트림을 복원
sys.stdout = original_stdout
