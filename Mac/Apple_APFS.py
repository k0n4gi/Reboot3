import subprocess
import re

def find_apfs_partition():
    cmd_output = subprocess.check_output(['diskutil', 'list']).decode('utf-8')
    
    # diskutil list의 출력에서 Apple_APFS 파티션을 찾는 정규 표현식 사용
    matches = re.findall(r'(/dev/disk\d+s\d+)\s+Apple_APFS', cmd_output)

    if matches:
        return matches[0]
    else:
        return None

def dump_partition(partition, output_file="APPLE_APFS.raw"):
    # dd 명령어를 사용하여 파티션을 덤프
    cmd = ["sudo", "dd", "if=" + partition, "of=" + output_file, "bs=1M"]
    subprocess.run(cmd)

def main():
    partition = find_apfs_partition()
    
    if partition:
        print(f"Found APFS partition: {partition}. Dumping to dump.raw...")
        dump_partition(partition)
        print("Dump complete.")
    else:
        print("APFS partition not found.")

if __name__ == "__main__":
    main()
