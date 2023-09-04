import subprocess

def get_patch_list():
    try:
        # 'softwareupdate' 명령어를 사용하여 패치 리스트 가져오기
        command = "softwareupdate --list"
        result = subprocess.check_output(command, shell=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

patch_list = get_patch_list()

# 결과를 'patch_list.txt' 파일에 저장
filename = './Mac/mac_result/patch_list.txt'
with open(filename, 'w') as file:
    file.write(patch_list)

print("패치 리스트가 'patch_list.txt' 파일에 저장되었습니다.")
