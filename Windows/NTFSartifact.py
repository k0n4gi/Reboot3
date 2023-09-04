import os
import subprocess

def collect_ntfs_artifacts():
    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    
    # 복사할 NTFS 시스템 파일
    ntfs_files = ["$MFT", "$LogFile", "$Extend\\$UsnJrnl:$J"]
    
    for ntfs_file in ntfs_files:
        source_file = "C:\\" + ntfs_file
        destination_file_name = ntfs_file.replace('$', '').replace(':', '').replace('\\', '_') + ".txt"
        destination_file = os.path.join(desktop, destination_file_name)
        
        command = "fsutil file queryextents {} > {}".format(source_file, destination_file)
        
        try:
            subprocess.run(command, shell=True, check=True, stderr=subprocess.PIPE)
            print("{}를 성공적으로 복사했습니다.".format(source_file))
        except subprocess.CalledProcessError as e:
            print("{}를 복사하는 데 실패했습니다: {}".format(source_file, e.stderr.decode('utf-8')))

if __name__ == "__main__":
    collect_ntfs_artifacts()
