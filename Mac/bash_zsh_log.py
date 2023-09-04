import os

# 사용자 홈 디렉터리
user_home = os.path.expanduser('~')

# Bash history 파일 경로
bash_history_path = os.path.join(user_home, '.bash_history')

# Zsh history 파일 경로
zsh_history_path = os.path.join(user_home, '.zsh_history')

# .bash_history 파일 읽기
bash_commands = []
if os.path.exists(bash_history_path):
    try:
        with open(bash_history_path, 'r', encoding='ISO-8859-1') as bash_history_file:
            bash_commands = bash_history_file.readlines()
    except UnicodeDecodeError:
        print(".bash_history: Unable to decode using ISO-8859-1")

# .zsh_history 파일 읽기
zsh_commands = []
if os.path.exists(zsh_history_path):
    try:
        with open(zsh_history_path, 'r', encoding='ISO-8859-1') as zsh_history_file:
            zsh_commands = zsh_history_file.readlines()
    except UnicodeDecodeError:
        print(".zsh_history: Unable to decode using ISO-8859-1")

# 결과를 텍스트 파일에 저장
bash_output_path = "./Mac/mac_result/bash_history.txt"
zsh_output_path = "./Mac//mac_result/zsh_history.txt"

with open(bash_output_path, 'w') as bash_output_file:
    for command in bash_commands:
        bash_output_file.write(command)

with open(zsh_output_path, 'w') as zsh_output_file:
    for command in zsh_commands:
        zsh_output_file.write(command)

print("Bash history saved to", bash_output_path)
print("Zsh history saved to", zsh_output_path)
