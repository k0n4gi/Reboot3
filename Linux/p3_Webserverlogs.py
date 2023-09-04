import os
from datetime import datetime

def collect_webserver_logs(log_paths, output_path):
    # 현재 시간을 포맷팅하여 문자열로 저장
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 결과 파일의 경로를 지정
    output_file = os.path.join(output_path, "webserver.txt")
    logs_collected = ""

    # 로그 경로 리스트를 순회하며 로그 파일 수집 작업 수행
    for log_path in log_paths:
        if os.path.exists(log_path):
            with open(log_path, "r") as log_file:
                logs_collected += f"====== {log_path} ======\n\n"
                logs_collected += log_file.read() + "\n\n"
                print(f"로그 파일 수집 완료: {log_path}")
        else:
            print(f"로그 파일을 찾을 수 없음: {log_path}")
    
    # 결과 파일에 로그 수집 날짜와 수집한 로그 내용 저장
    with open(output_file, "w") as output_file:
        output_file.write(f"웹 서버 로그 수집일: {current_time}\n\n")
        output_file.write(logs_collected)
    
    print(f"로그 파일을 {output_file}에 저장 완료")

if __name__ == "__main__":
    # 웹 서버 로그 파일 경로 리스트 설정
    webserver_log_paths = [
        "/var/log/apache2/access.log",   # Apache 웹 서버 접근 로그
        "/var/log/apache2/error.log",    # Apache 웹 서버 에러 로그
        "/var/log/nginx/access.log",     # Nginx 웹 서버 접근 로그
        "/var/log/nginx/error.log",      # Nginx 웹 서버 에러 로그
        "/var/log/lighttpd/access.log",  # Lighttpd 웹 서버 접근 로그
        "/var/log/lighttpd/error.log"    # Lighttpd 웹 서버 에러 로그
        # 추가로 웹 서버 로그 파일 경로를 필요에 맞게 추가합니다.
    ]
    
    # 로그 파일 결과가 저장될 디렉터리 경로 설정
    output_directory = "/mnt/c/Users/USER/Desktop/구름프로젝트3-2/Reboot3/Linux"
    
    # 웹 서버 로그 수집 함수 호출
    collect_webserver_logs(webserver_log_paths, output_directory)