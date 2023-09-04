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
    # 'mac_result' 폴더 생성 혹은 확인
    results_folder = 'mac_result'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    start_time = input("Enter the start time for log collection (format: 'yyyy-mm-dd hh:mm:ss'): ")
    end_time = input("Enter the end time for log collection (format: 'yyyy-mm-dd hh:mm:ss'): ")

    logs = collect_logs(start_time, end_time)
    
    if logs:
        # 결과값 저장 경로를 'mac_result' 폴더 내로 지정
        result_file_path = os.path.join(results_folder, "collected_logs.txt")
        with open(result_file_path, 'w') as file:
            file.write(logs)
        
        print(f"Logs collected and saved to {result_file_path}.")

if __name__ == "__main__":
    main()
