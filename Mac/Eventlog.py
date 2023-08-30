#이벤트 로그 수집기, 원하는 시간대를 설정하여 로그 수집 가능 기본적으로 바탕화면에 저장하는 형태
#타임 스탬프, 시스템 정보(부팅 및 종료 시간, 시스템 업데이트, 하드웨어 상태),응용 프로그램 및 서비스 로그, 보안정보(로그인 시도, 권한 변경), 네트워크 활동
import subprocess
import os

def collect_logs(start_time, end_time):
    # 'log show' 명령어를 사용하여 로그 수집
    command = [
        'log', 'show', 
        '--start', start_time,
        '--end', end_time
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout
    else:
        print(f"Error collecting logs: {result.stderr}")
        return None

def main():
    start_time = input("Enter the start time for log collection (format: 'yyyy-mm-dd hh:mm:ss'): ")
    end_time = input("Enter the end time for log collection (format: 'yyyy-mm-dd hh:mm:ss'): ")

    logs = collect_logs(start_time, end_time)
    
    if logs:
        # 바탕화면에 파일로 저장
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        with open(os.path.join(desktop_path, "collected_logs.txt"), 'w') as file:
            file.write(logs)
        
        print("Logs collected and saved to your desktop.")

if __name__ == "__main__":
    main()
