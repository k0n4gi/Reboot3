import os
import shutil  
from datetime import datetime

def collect_antivirus_logs(logs_to_collect, destination_path):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = os.path.join(destination_path, f"antivirus_logs_{current_time}")
    os.makedirs(output_dir, exist_ok=True)  # 저장할 디렉토리를 생성합니다
    
    # 로그 파일들을 모두 지정된 목적 경로에 복사하여 저장합니다
    for antivirus, log_file in logs_to_collect.items():
        if os.path.exists(log_file):
            log_filename = os.path.basename(log_file)
            destination_file = os.path.join(output_dir, f"{antivirus}_{log_filename}.txt")
            shutil.copy(log_file, destination_file)  # 로그 파일을 목적 경로로 복사합니다
            print(f"수집 완료: {log_file} -> {destination_file}")  # 수집 완료 메시지 출력
        else:
            print(f"로그 파일을 찾을 수 없음: {log_file}")  # 로그 파일이 없을 경우 메시지 출력

if __name__ == "__main__":
    logs_to_collect = {
        "ClamAV": "/var/log/clamav/clamav.log",
        "Sophos": "/var/log/sophos.log",
        "ESET": "/var/log/eset.log",
        "Bitdefender": "/var/log/bitdefender.log",
        "Avira": "/var/log/avira.log",
        "F-Prot": "/var/log/f-prot.log",
        "chkrootkit": "/var/log/chkrootkit.log",
        # 추가 리눅스용 백신 로그 파일 경로 추가 가능
    }
    
    # 저장할 목적지 경로를 지정합니다. 수정이 필요합니다.
    destination_path = "C:\\Users\\USER\\Desktop\\구름프로젝트3-2\\Reboot3\\Linux"  # 실제 저장 경로로 수정해야 함
    
    # 로그 파일들을 모두 지정된 목적 경로에 복사하여 저장합니다
for antivirus, log_file in logs_to_collect.items():
    if os.path.exists(log_file):
        log_filename = os.path.basename(log_file)
        destination_file = os.path.join(destination_path, f"{antivirus}_{log_filename}.txt")
        shutil.copy(log_file, destination_file)  # 로그 파일을 목적 경로로 복사합니다
        print(f"수집 완료: {log_file} -> {destination_file}")  # 수집 완료 메시지 출력
    else:
        print(f"로그 파일을 찾을 수 없음: {log_file}")  # 로그 파일이 없을 경우 메시지 출력