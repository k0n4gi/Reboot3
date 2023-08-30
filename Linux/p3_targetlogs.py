import os
import logging
from configparser import ConfigParser

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 외부 설정 파일에서 로그 파일 목록을 가져오기
def load_target_logs(config_file=None):
    if config_file is None:
        # 현재 스크립트의 절대 경로를 구하고, 그 디렉토리를 기준으로 설정 파일을 찾는다.
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(script_dir, "log_files.ini")
    
    config = ConfigParser()
    try:
        config.read(config_file)
        return config.get("logs", "target_logs").split(",")
    except Exception as e:
        logger.error(f"Error reading configuration from {config_file}: {str(e)}")
        return []

def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        logger.error(f"{filepath} not found.")
    except PermissionError:
        logger.error(f"Permission denied for {filepath}.")
    except Exception as e:
        logger.error(f"Error reading {filepath}: {str(e)}")
    return []

def get_log_files(directory):
    target_logs = load_target_logs()
    return [os.path.join(directory, log) for log in target_logs]

def main():
    files = get_log_files("/var/log/")
    
    for filepath in files:
        lines = read_file(filepath)
        
        print(f"=== Contents of {filepath} ===")
        for idx, line in enumerate(lines, 1):
            print(f"{idx:04d}: {line.strip()}")
        print("="*40)

if __name__ == "__main__":
    main()
