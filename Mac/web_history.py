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

####운영체제 버전 정보 저장

destination_dir= "./web_history"  # 추출된 데이터가 저장될 디렉토리
if not os.path.exists(destination_dir):
    os.mkdir(destination_dir)



#####################사파리 정보 

#####Bookmarks.plist
try:
# 파일 복사
    source_path = f"/Users/{username}/Library/Safari/Bookmarks.plist"  # 복사할 대상
    destination_path = "./web_history/Bookmarks.plist"#저장소

    # 파일이 이미 존재하면 삭제
    if os.path.exists(destination_path):
        os.remove(destination_path)
        print(f"Existing file '{destination_path}' removed.")

    shutil.copy(source_path, destination_path)
    
    print( f"/Users/{username}/Library/web_history/Bookmarks.plist이 복사되었습니다" )
except:  
        print( f"Bookmarks.plist에 실패했습니다" )


####historyDB복사
try:
    source_path = f"/Users/{username}/Library/Safari/History.db"  # 복사할 대상
    destination_path = "./web_history/History.db"#저장소

    # 파일이 이미 존재하면 삭제
    if os.path.exists(destination_path):
        os.remove(destination_path)
        print(f"Existing file '{destination_path}' removed.")
        
    shutil.copy(source_path, destination_path)
    
    print( f"/Users/{username}/Library/safari/History.db가 복사되었습니다" )
except:  
        print( f"History.db 저장에 실패했습니다" )

####historyDB복사
try:
    source_path = f"/Users/{username}/Library/Safari/Downloads.plist"  # 복사할 대상
    destination_path = "./web_history/Downloads.plist"#저장소

    # 파일이 이미 존재하면 삭제
    if os.path.exists(destination_path):
        os.remove(destination_path)
        print(f"Existing file '{destination_path}' removed.")
        
    shutil.copy(source_path, destination_path)
    
    print( f"/Users/{username}/Library/safari/Downloads.plist가 복사되었습니다" )
except:  
        print( f"Downloads.plist 저장에 실패했습니다" )

##############구글 크롬 정보

try:
    source_path = f"/Users/{username}/Library/Application Support/Google/Chrome/Default/History"  # 복사할 대상
    destination_path = "./web_history/chrome_History"#저장소
    

    # 파일이 이미 존재하면 삭제
    if os.path.exists(destination_path):
        os.remove(destination_path)
        print(f"Existing file '{destination_path}' removed.")
        
    shutil.copy(source_path, destination_path)
    
    print( f"/Users/{username}/Library/Application Support/Google/Chrome/Default/History가 복사되었습니다" )
except:  
        print( f"크롬 히스토리 저장에 실패했습니다" )