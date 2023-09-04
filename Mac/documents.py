import os

# 문서 파일 확장자 리스트
document_extensions = ['txt', 'doc', 'docx', 'pdf', 'ppt', 'pptx', 'odt', 'md', 'rst', 'pages', 'xlsx', 'ods', 'numbers', 'odp', 'key', 'cpp', 'java', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'webp', 'ico', 'exif', 'raw', 'exp', 'class', 'app', 'sh', 'bat', 'jar', 'pyc', 'py', 'js', 'rb', 'pl', 'sql', 'c', 'cpp', 'cs', 'java', 'cs', 'go', 'xml', 'yaml', 'log', 'cfg', 'csv', 'ini', 'sql','hwp']

# 검색할 디렉터리 경로 설정
search_directory = '/'  # 실제 디렉터리 경로로 바꿔주세요
output_file_path = './Mac/mac_result/document_files.txt'  # 결과를 저장할 텍스트 파일 경로

# 모든 문서 파일 목록을 저장할 리스트
document_files = []

# 디렉터리 내의 모든 파일과 하위 디렉터리 검색
for root, dirs, files in os.walk(search_directory):
    for file in files:
        # 파일의 확장자 추출
        file_extension = file.split('.')[-1]

        # 추출한 확장자가 문서 확장자 리스트에 포함되어 있는지 확인
        if file_extension in document_extensions:
            # 문서 파일의 절대 경로 생성
            document_path = os.path.join(root, file)

            # 절대 경로를 리스트에 추가
            document_files.append(document_path)

# 결과를 텍스트 파일로 저장
with open(output_file_path, 'w') as f:
    for document_path in document_files:
        f.write(document_path + '\n')

print("Document files list saved to", output_file_path)
