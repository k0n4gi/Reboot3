import subprocess

def save_launchctl_list_to_file(filename):
    # launchctl list 명령어를 실행합니다.
    result = subprocess.run(["launchctl", "list"], capture_output=True, text=True)

    if result.returncode != 0:
        print("Error:", result.stderr)
        return

    # 결과를 파일에 저장합니다.
    with open(filename, 'w') as f:
        f.write(result.stdout)

# 실행 예제
save_launchctl_list_to_file("launch_list.txt")
