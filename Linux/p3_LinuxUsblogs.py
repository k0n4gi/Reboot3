import subprocess
import os

def collect_usb_logs(output_file):
    # USB 연결 로그를 시스템 로그에서 추출하는 명령어
    command = "grep 'usb' /var/log/syslog"

    try:
        # 명령어 실행 및 결과 가져오기
        result = subprocess.check_output(command, shell=True, universal_newlines=True)

        # 결과를 지정한 파일에 저장
        with open(output_file, 'w') as f:
            f.write(result)

        print(f"USB logs collected and saved to {output_file}")

    except subprocess.CalledProcessError:
        print("Error collecting USB logs.")

if __name__ == "__main__":
    # 리눅스 경로로 변환하여 사용
    linux_desktop_path = "/mnt/c/Users/USER/Desktop/구름프로젝트3-2/Reboot3/Linux"
    
    # usb_logs.txt 파일 경로 생성
    output_file_path = os.path.join(linux_desktop_path, "usb_logs.txt")

    # USB 로그 수집 및 파일에 저장
    collect_usb_logs(output_file_path)
