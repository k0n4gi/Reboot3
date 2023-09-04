import subprocess

# launchctl list 명령어 실행하여 결과 가져오기
command = ["launchctl", "list"]
result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

# 결과를 txt 파일로 저장하기
filename = './Mac/mac_result/service_demon.txt'
with open(filename, "w") as f:
    f.write(result.stdout)

print("service_demon.py.txt 파일로 저장되었습니다.")
