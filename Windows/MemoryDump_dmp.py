import shutil
import os

# 원본 Memory.dmp 파일 경로
source_path = os.path.join(os.environ['SystemRoot'], 'Memory.dmp')

# 사용자의 바탕화면 경로
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')

# 복사될 Memory.dmp 파일 경로
destination_path = os.path.join(desktop_path, 'Memory.dmp')

# Memory.dmp 파일을 바탕화면으로 복사
try:
    shutil.copy(source_path, destination_path)
    print(f"{source_path}를 {destination_path}로 복사 완료.")
except PermissionError:
    print("관리자 권한이 필요합니다.")
except FileNotFoundError:
    print("원본 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"파일 복사 중 오류 발생: {e}")
