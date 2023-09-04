import psutil
import os

def collect_process_info():
    process_info_list = []

    for process in psutil.process_iter(attrs=['pid', 'name', 'username', 'memory_info']):
        info = process.info
        pid = info['pid']
        name = info['name']
        username = info['username']
        memory = info['memory_info'].rss  # Resident Set Size: 메모리 사용량

        process_info = f"PID: {pid}, Process Name: {name}, User: {username}, Memory: {memory} bytes"
        process_info_list.append(process_info)

    return process_info_list

if __name__ == "__main__":
    # 바탕화면 경로 설정
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    # .txt 파일로 저장될 경로 설정
    file_path = os.path.join(desktop, "process_list.txt")

    process_list = collect_process_info()

    with open(file_path, 'w') as f:
        for process in process_list:
            f.write(process + '\n')

    print(f"실행 중인 프로세스 정보가 {file_path} 에 저장되었습니다.")
