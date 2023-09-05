import os

def read_bash_history(file_path="~/.bash_history"):
    file_path = os.path.expanduser(file_path) # 홈 디렉토리(~) 경로를 전체 경로로 확장합니다.
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    return lines

# 명령어의 빈도를 분석하는 함수
def analyze_commands(commands):
    frequency = {} # 명령어의 빈도를 저장할 딕셔너리
    for cmd in commands:
        cmd = cmd.strip() # 앞뒤 공백을 제거
        if cmd in frequency: # 명령어가 이미 딕셔너리에 있다면
            frequency[cmd] += 1  # 빈도를 1 증가
        else:
            frequency[cmd] = 1 # 명령어가 딕셔너리에 없다면, 빈도를 1로 설정
    return frequency  # 분석 결과를 반환

if __name__ == "__main__":
    bash_history = read_bash_history()
    analysis_result = analyze_commands(bash_history)

    # 현재 디렉토리에 결과 파일 생성
    output_path = "collect_bashhistory.txt"

    # 결과를 파일에 쓰고, 콘솔에도 출력합니다.
    with open(output_path, 'w') as f:
        for cmd, freq in sorted(analysis_result.items(), key=lambda x: x[1], reverse=True): # 빈도수가 높은 순으로 정렬
            line = f"{cmd}: {freq}번"
            print(line)  # 출력창에 결과 출력
            f.write(line + "\n")
