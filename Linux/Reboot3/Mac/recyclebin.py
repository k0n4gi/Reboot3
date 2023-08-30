import os
import shutil

def get_username():
    return os.environ.get("USER") 

def save_ds_store(source_folder, output_path):
    ds_store_path = os.path.join(source_folder, ".DS_Store")
    if os.path.exists(ds_store_path):
        with open(ds_store_path, 'rb') as src_file, open(output_path, 'wb') as dest_file:
            dest_file.write(src_file.read())
        print(f".DS_Store file saved to {output_path}")
    else:
        print(f".DS_Store file not found in {source_folder}")

if __name__ == "__main__":
    username = get_username()  # 사용자 이름 얻어오기
    source_folder = f"/Users/{username}/Desktop"  # .DS_Store 파일이 있는 폴더 경로
    
    output_directory = "./trash_DSStore"  # 추출된 데이터가 저장될 디렉토리
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)
    
    output_path = os.path.join(output_directory, "DS_Store_copy")  # 저장될 파일 경로
    save_ds_store(source_folder, output_path)
