import os
import shutil
import subprocess

def get_current_user():
    result = subprocess.run(["whoami"], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()

username = get_current_user()  # 사용자 이름 얻어오기

if username=="root":
     while True:
         
         username=input("사용자가 root로 실행되었습니다. 히스토리를 가져올 대상의 사용자를 입력 후 엔터 :")
         ask=input(f"사용자가 {username}이 맞습니까  y/n   ")
         if ask=='y' or ask=="Y":
              break
         
destination_dir= "./Trash_DS"  # 추출된 데이터가 저장될 디렉토리
if not os.path.exists(destination_dir):
    os.mkdir(destination_dir)

#####Bookmarks.plist
try:
# 파일 복사
    source_path = f"/Users/{username}/.Trash/.DS_Store"  # 복사할 대상
    destination_path = "./Trash_DS/trash_DS_Store"#저장소

    # 파일이 이미 존재하면 삭제
    if os.path.exists(destination_path):
        os.remove(destination_path)
        print(f"Existing file '{destination_path}' removed.")

    shutil.copy(source_path, destination_path)
    
    print( f"/Users/{username}/.Trash/.DS_Store가 복사되었습니다." )
except:  
        print( f"Bookmarks.plist에 실패했습니다" )