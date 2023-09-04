import subprocess

def get_open_handles():
    open_handles = []

    # 'lsof' 명령 실행 및 결과 가져오기
    command = ["lsof"]
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = result.communicate()
    output_lines = output.decode("utf-8").splitlines()

    # 결과 파싱하여 열린 핸들 정보 추출
    for line in output_lines:
        parts = line.split()
        if len(parts) >= 2:
            handle_type = parts[0]
            handle_name = parts[-1]
            open_handles.append((handle_type, handle_name))

    return open_handles

def save_to_file(file_path, content):
          # 저장할 파일의 경로 지정
    file_path = './Mac/mac_result/open_handles.txt'  # 원하는 경로로 변경

    with open(file_path, 'w') as file:
        for handle_type, handle_name in content:
            file.write(f"Type: {handle_type} | Name: {handle_name}\n")

open_handles = get_open_handles()
save_to_file('open_handles.txt', open_handles)
print("열린 핸들 정보가 'open_handles.txt' 파일에 저장되었습니다.")
