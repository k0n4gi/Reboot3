import subprocess

def get_cron_jobs():
    try:
        output = subprocess.check_output(["crontab", "-l"], stderr=subprocess.STDOUT, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.strip()}"

def save_to_file(data, filename):
    with open(filename, "w") as f:
        f.write(data)

if __name__ == "__main__":
    cron_jobs = get_cron_jobs()
    
    if not cron_jobs.startswith("Error"):
        save_to_file(cron_jobs, "crone.txt")  # 수정된 부분: 파일 이름을 "crone.txt"로 변경
        print("Cron jobs saved to crone.txt")  # 수정된 부분: 메시지 수정
    else:
        print(cron_jobs)
