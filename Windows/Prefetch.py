import os

# Prefetch 폴더 경로
prefetch_path = r"C:\Windows\Prefetch"

# 바탕화면에 저장될 .txt 파일 경로
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
output_file_path = os.path.join(desktop, "prefetch_info.txt")

# Prefetch 폴더에서 .pf 파일 목록 수집
try:
    prefetch_files = [f for f in os.listdir(prefetch_path) if f.endswith('.pf')]
except PermissionError:
    print("관리자 권한이 필요합니다.")
    exit()

# 수집된 정보를 .txt 파일로 저장
try:
    with open(output_file_path, "w") as f:
        for prefetch_file in prefetch_files:
            f.write(prefetch_file + "\n")
    print(f"정보가 성공적으로 저장되었습니다: {output_file_path}")
except Exception as e:
    print(f"파일을 저장하는 중에 오류가 발생했습니다: {e}")
