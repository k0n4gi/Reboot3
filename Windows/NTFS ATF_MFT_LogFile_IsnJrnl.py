# 이 코드는 pytsk3 라이브러리가 필요하며, 관리자 권한으로 실행해야 할 수도 있습니다.
# pip install pytsk3

import pytsk3
import os

# 바탕화면에 저장될 .txt 파일 경로
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
output_file_path = os.path.join(desktop, "NTFS_Artifacts_Info.txt")

try:
    with open(output_file_path, "w") as f:
        # $MFT 정보를 수집하는 예시 (구현은 간단하게 유지)
        f.write("=== $MFT Information ===\n")
        # ... 여기에 $MFT 정보 수집 코드
        f.write("\n")

        # $LogFile 정보를 수집하는 예시
        f.write("=== $LogFile Information ===\n")
        # ... 여기에 $LogFile 정보 수집 코드
        f.write("\n")

        # $UsnJrnl 정보를 수집하는 예시
        f.write("=== $UsnJrnl Information ===\n")
        # ... 여기에 $UsnJrnl 정보 수집 코드
        f.write("\n")

    print(f"정보가 성공적으로 저장되었습니다: {output_file_path}")

except Exception as e:
    print(f"파일을 저장하는 중에 오류가 발생했습니다: {e}")
