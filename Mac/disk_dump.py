# 디스크 덤프 파일 %%실행 전 주의 사항%%
# 1. brew install ddrescue << 설치
# 2. Mac을 재부팅하고, 부팅 동안 Command + R 키를 함께 눌러서 복구 모드(Recovery Mode)로 진입
# 3. 상단 메뉴에서 유틸리티 > 터미널을 선택
# 4. 터미널에서 'csrutil disable' 명령을 실행하여 SIP을 비활성화
# 5. Mac을 정상적으로 재부팅합니다.
# 6. 이미징 후에 위의 절차를 따라 한 후 'csrutil enable' 명령을 실행
# %%주의%% : SIP은 Mac의 보안 기능 중 하나입니다. 작업이 끝나면 반드시 다시 활성화해주세요
import os
import subprocess

def ddrescue_disk(source_path, destination_path):
    """
    원본 경로(디스크/파티션)에서 데이터를 덤프하여 대상 경로(출력 파일)에 저장합니다.
    """
    command = ["ddrescue", "-f", source_path, destination_path]
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"{source_path}에서 {destination_path}로 덤프하는 중 오류가 발생했습니다.")
        print(result.stderr)
    else:
        print(f"{source_path}에서 {destination_path}로 데이터를 dump했습니다.")

def get_all_disks():
    """컴퓨터에 연결된 모든 디스크의 목록을 반환합니다."""
    output = subprocess.check_output(["diskutil", "list"], universal_newlines=True)
    disks = []
    
    for line in output.split("\n"):
        if "/dev/disk" in line:
            disk_path = line.strip().split()[0]
            disks.append(disk_path)
    return disks

if __name__ == '__main__':
    # 'mac_result' 폴더 생성 혹은 확인
    results_folder = 'mac_result'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    # 모든 디스크 목록을 가져옵니다.
    all_disks = get_all_disks()
    
    # 각 디스크를 덤프합니다.
    for disk in all_disks:
        destination = os.path.join(results_folder, f"{os.path.basename(disk)}_dump.img")
        ddrescue_disk(disk, destination)
    
    print("이미징이 완료되었습니다.")
