import subprocess

def execute_command(cmd):
    try:
        return subprocess.run(cmd, stdout=subprocess.PIPE, text=True).stdout
    except Exception as e:
        return f"Error executing {cmd}: {str(e)}"

if __name__ == "__main__":
    # SELinux 로그 파일 경로
    selinux_log_path = "/var/log/audit/audit.log"

    # 로그 파일의 내용을 읽는 명령어 설정
    read_log_cmd = ["cat", selinux_log_path]

    # 명령어 실행 및 결과 수집
    log_content = execute_command(read_log_cmd)

    # 결과를 터미널에 출력
    print("=== SELinux/앱아머 로그 내용 ===")
    print(log_content)

    # 결과를 .txt 파일에 저장
    with open("SELinux_Audit_Log.txt", "w") as f:
        f.write("=== SELinux/앱아머 로그 내용 ===\n")
        f.write(log_content)
