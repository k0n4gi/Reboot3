import subprocess
import os

# PowerShell 명령어를 실행하여 로그온 정보를 가져옵니다.
command = 'wevtutil qe Security /q:"*[System[Provider[@Name=\'Microsoft-Windows-Security-Auditing\'] and (EventID=4624)]]" /c:10 /rd:true /f:text'
result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)

# 결과를 바탕화면의 .txt 파일에 저장합니다.
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, 'logon_info.txt')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(result.stdout)

print(f"로그온 정보가 {file_path}에 저장되었습니다.")
import subprocess
import os

def get_logon_history():
    query = "wevtutil qe Security /q:\"*[System[Provider[@Name='Microsoft-Windows-Security-Auditing'] and (EventID=4624)]]\" /c:1 /rd:true /f:text"
    result = subprocess.run(query, capture_output=True, text=True, shell=True)
    return result.stdout

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
    file_path = os.path.join(desktop_path, "logon_history.txt")

    logon_history = get_logon_history()

    with open(file_path, 'w') as f:
        f.write(logon_history)

    print(f"Logon history has been saved to {file_path}")
