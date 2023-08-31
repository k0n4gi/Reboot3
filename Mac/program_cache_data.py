#애플리케이션 캐시, 시스템 캐시를 가져오는 코드
import os
import tarfile

def backup_cache_data(output_filename="caches.tar.gz"):
    # 사용자의 홈 디렉토리를 가져옵니다.
    home_directory = os.path.expanduser("~")
    cache_directory = os.path.join(home_directory, "Library", "Caches")
    
    # 지정된 출력 파일 이름으로 tar.gz 압축 파일을 생성합니다.
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(cache_directory, arcname="Caches")

    print(f"Backup completed! Saved to {output_filename}")

# 실행 예제
backup_cache_data()
