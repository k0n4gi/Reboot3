import subprocess

# Linux 명령어와 해당 명령어의 라벨을 저장하는 딕셔너리
commands_labels = {
    # 1. 기본 시스템 정보
    "=== Linux System Info ===": ['uname', '-a'],
    "=== Linux System Date Info ===": ['date'],
    "=== Linux Hard Clock Info ===": ['hwclock', '--verbose'],
    "=== Linux CPU Info ===": ['lscpu'],
    "=== Linux Block Device Info ===": ['lsblk'],
    "=== Linux Memory Using Info ===": ['free', '-h'],
    "=== Linux Environment Variables ===": ['env'],

    # 2. 사용자와 인증 정보
    "=== Linux User Info ===": ['cat', '/etc/passwd', 'cat', '/etc/shadow', 'cat', '/etc/group'],
    "=== Linux SSH Access History Info ===": ['cat', '/var/log/auth.log'],
	"=== Linux Bash History ===": ['cat', '~/.bash_history'],

    # 3. 네트워크 정보
    "=== Linux Network Info ===": ['ip', 'addr'],
    "=== Linux Network Active Connections ===":['netstat', '-tuln'],
    "=== Linux ARP Table Info ===": ['ip', 'neigh'],
    "=== Linux Iptables Rules ===": ['sudo','iptables','-L'],

    # 4. 실행 중인 프로세스 및 서비스 정보
    "=== Linux Process Info ===": ['ps', 'aux'],
    "=== Linux Activated Services Info ===": ['systemctl', 'list-units', '--type=service'],
    "=== Linux System Startup Programs ===": ['systemctl', 'list-unit-files'],

    # 5. 디스크와 파일 시스템 정보
    "=== Linux Disk Using Info ===": ['df', '-h'],
    "=== Linux Mount Files Info ===": ['mount'],
    "=== Linux PCI Connecting Device Info ===": ['lspci'],
	"=== Linux Trash Info ===": ['ls', '~/.local/share/Trash/files/'],

    # 6. 로그 정보
    "=== Linux System Logs ===": ['cat', '/var/log/syslog'],
    "=== Linux Kernel Logs ===": ['cat', '/var/log/kern.log'],
    "=== Linux Boot Logs ===": ['cat', '/var/log/boot.log'],
    "=== Linux Daemon Logs ===": ['cat', '/var/log/daemon.log'],
    "=== Linux Cron Jobs ===": ['cat', '/etc/crontab', 'ls', '/var/spool/cron/'],
	"=== Linux SELinux Logs ===": ['cat', '/var/log/audit/audit.log'], 
	"=== Linux Web Server Logs ===": ['cat', '/var/log/apache2/access.log', 'cat', '/var/log/apache2/error.log'],
	"=== Linux Mail Server Logs ===": ['cat', '/var/log/mail.log'], 
	"=== Linux USB Logs ===": ['dmesg', '|', 'grep', 'usb']
}

# 주어진 명령어를 실행하고 그 결과를 반환하는 함수
def execute_command(cmd):
    try:
        return subprocess.run(cmd, stdout=subprocess.PIPE, text=True).stdout
    except Exception as e:
        return f"Error executing {cmd}: {str(e)}"
		
# 결과를 저장하기 위한 변수 초기화
output = ""

# 각 명령어를 실행하고 그 결과와 라벨을 출력한 후, 결과 리스트에 저장
for label, cmd in commands_labels.items():
    result = f"{label}\n\n{execute_command(cmd)}"
    print(result)
    output += result + "\n\n"

# 결과를 'forensics_output.txt' 파일에 저장
with open('/tmp/forensics_output.txt', 'w', encoding='utf-8') as f:
    f.write(output)
    print('/tmp 경로 아래에 결과 파일을 저장했습니다.')