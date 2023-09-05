# Python 코드 예시: tcpdump을 사용하여 네트워크 패킷을 수집하는 코드
import subprocess
import sys
import os

def execute_command(cmd):
    # subprocess를 사용하여 쉘 명령어를 실행하고 결과를 반환합니다.
    try:
        return subprocess.run(cmd, stdout=subprocess.PIPE, text=True).stdout
    except Exception as e:
        return f"Error executing {cmd}: {str(e)}"

if __name__ == "__main__":
    
    # 루트 권한 확인
    if os.geteuid() != 0:
        print("이 스크립트는 루트 권한으로 실행되어야 합니다.")
        sys.exit(1)

    # tcpdump 명령어를 설정합니다. 이 예제에서는 첫 10개의 패킷만 수집합니다.
    # 실제 사용 시에는 이 옵션을 적절히 조정해야 합니다.
    tcpdump_cmd = ["tcpdump", "-c", "10"]

    # 명령어 실행 및 결과 수집
    packet_data = execute_command(tcpdump_cmd)

    # 결과를 터미널에 출력
    print("=== tcpdump 네트워크 패킷 데이터 ===")
    print(packet_data)

    # 결과를 .txt 파일에 저장
    with open("Network_Packet_Data.txt", "w") as f:
        f.write("=== tcpdump 네트워크 패킷 데이터 ===\n")
        f.write(packet_data)

