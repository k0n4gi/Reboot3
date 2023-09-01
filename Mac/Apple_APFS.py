# 코드를 진행하기 전 해결 사항
# 1. 시스템 환경설정
# 2. 보안 및 개인 정보 보호
# 3. 전체 디스크 접근 권한
# 4. Terminal 관련 앱 권한 승인
# 5. diskutil list 명령어로 APFS 디스크 찾은 후 해당 APFS dump 진행
# 6. 보통 APFS는 /dev/disk0s2 입니다.

import subprocess

def dump_partition(partition, output_file="APPLE_APFS.raw"):
    # dd 명령어를 사용하여 파티션을 덤프
    cmd = ["sudo", "dd", "if=" + partition, "of=" + output_file, "bs=1M"]
    subprocess.run(cmd)

def main():
    partition = input("Please enter the APFS partition identifier (e.g., /dev/disk0s2): ")
    
    if partition:
        print(f"Dumping {partition} to APPLE_APFS.raw...")
        dump_partition(partition)
        print("Dump complete.")
    else:
        print("Invalid partition identifier.")

if __name__ == "__main__":
    main()
