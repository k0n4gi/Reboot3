# Python 코드 예시: 메일 로그 파일의 존재 여부 확인 및 루트 권한 확인
import os
import subprocess
import sys

# 명령어를 실행하고 결과를 반환하는 함수
def execute_command(cmd):
    try:
        return subprocess.run(cmd, stdout=subprocess.PIPE, text=True).stdout
    except Exception as e:
        return f"Error executing {cmd}: {str(e)}"

if __name__ == "__main__":
    # 출력될 파일의 경로 설정
    output_file_path = "/mnt/c/Users/USER/Desktop/구름프로젝트3-2/Reboot3/Linux/Mail_Server_Log.txt"

    # 메일 로그 파일 경로
    mail_log_path = "/var/log/mail.log"

    # 루트 권한 확인
    if os.geteuid() != 0:
        print("이 스크립트는 루트 권한으로 실행되어야 합니다.")
        sys.exit(1)

    # 로그 파일 존재 여부 확인
    if not os.path.exists(mail_log_path):
        print(f"{mail_log_path} 파일이 존재하지 않습니다.")
        sys.exit(1)

    # 로그 파일의 내용을 읽는 명령어 설정
    read_log_cmd = ["cat", mail_log_path]

    # 명령어 실행 및 결과 수집
    log_content = execute_command(read_log_cmd)

    # 결과를 터미널에 출력
    print("=== 메일 서버 로그 내용 ===")
    print(log_content)

    # 결과를 .txt 파일에 저장
    with open(output_file_path, "w") as f:
        f.write("=== 메일 서버 로그 내용 ===\n")
        f.write(log_content)
