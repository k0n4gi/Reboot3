import os

def read_bash_history(file_path="~/.bash_history"):
    file_path = os.path.expanduser(file_path)
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    return lines

def analyze_commands(commands):
    frequency = {}
    for cmd in commands:
        cmd = cmd.strip()
        if cmd in frequency:
            frequency[cmd] += 1
        else:
            frequency[cmd] = 1
    return frequency

if __name__ == "__main__":
    bash_history = read_bash_history()
    analysis_result = analyze_commands(bash_history)

    # 현재 디렉토리에 결과 파일 생성
    output_path = "collect_bashhistory.txt"

    with open(output_path, 'w') as f:
        for cmd, freq in sorted(analysis_result.items(), key=lambda x: x[1], reverse=True):
            line = f"{cmd}: {freq}번"
            print(line)  # 출력창에 결과 출력
            f.write(line + "\n")
