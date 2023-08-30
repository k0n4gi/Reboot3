import os

def save_environment_variables_to_file(filename):
    environment_variables = os.environ

    with open(filename, 'w') as file:
        file.write("환경 변수:\n")
        for variable, value in environment_variables.items():
            file.write(f"{variable} = {value}\n")

    print(f"환경 변수가 '{filename}' 파일에 저장되었습니다.")

if __name__ == "__main__":
    save_environment_variables_to_file('environment_variables.txt')
