import os
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

def main():
    # 'mac_result' 폴더 생성 혹은 확인
    results_folder = 'mac_result'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    # 결과값 저장 경로를 'mac_result' 폴더 내로 지정
    output_file_path = os.path.join(results_folder, "launch_list.txt")

    save_launchctl_list_to_file(output_file_path)
    print(f"Launchctl list saved to {output_file_path}.")

if __name__ == "__main__":
    main()
