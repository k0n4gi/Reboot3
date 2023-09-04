import os
import subprocess

def dump_partition(partition, output_file):
    # dd 명령어를 사용하여 파티션을 덤프
    cmd = ["sudo", "dd", "if=" + partition, "of=" + output_file, "bs=1M"]
    subprocess.run(cmd)

def main():
    # 'mac_result' 폴더 생성 혹은 확인
    results_folder = 'mac_result'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    # 결과값 저장 경로를 'mac_result' 폴더 내로 지정
    output_file_path = os.path.join(results_folder, "APPLE_APFS.raw")

    partition = input("Please enter the APFS partition identifier (e.g., /dev/disk0s2): ")
    
    if partition:
        print(f"Dumping {partition} to {output_file_path}...")
        dump_partition(partition, output_file_path)
        print("Dump complete.")
    else:
        print("Invalid partition identifier.")

if __name__ == "__main__":
    main()
