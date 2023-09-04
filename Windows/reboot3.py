from pyfiglet import Figlet
import LnkParse3
import os
from shutil import copyfile
import shutil
from guppy import hpy
import sqlite3
import subprocess
import winreg
import base64
import subprocess

def init():
	f = Figlet(font='slant')
	print(f.renderText('Reboot'))
	print("This program is Artifact collecter\n")

def showOptions():
	print("\n==========Options==========")
	print("1) Memory Dump")
	print("2) Registry Hive")
	print("3) System Info")
	print("4) System Audit Policy")
	print("5) Group Policy")
	print("6) Event Viewer Log")
	print("7) Services Log")
	print("8) Hosts Data")
	print("9) SRUM (System Resource Utilization Monitor)")
	print("10) Environment Variables")
	print("11) Patch List")
	print("20) UserAssist")
	print("21) AutoRun")
	print("22) Registry User")
	print("23) Internet Browser History")
	print("24) Recycle Bin")
	print("25) LNK File")
	print("26) PowerShell Log File")
	print("0) exit program")

def registryHive():
	print("\n==========Registry Hive File==========")
	current_directory = os.getcwd()

	export_registry_hive(current_directory, winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE")
	export_registry_hive(current_directory, winreg.HKEY_CURRENT_USER, r"Software")

def export_registry_hive(output_directory, hive_name, hive_path):
    registry_folder = os.path.join(output_directory, "RegistryHive")
    if not os.path.exists(registry_folder):
        os.makedirs(registry_folder)

    try:
        with winreg.ConnectRegistry(None, hive_name) as hive:
            hive_output_file = os.path.join(registry_folder, f"{hive_name}_hive.txt")

            with open(hive_output_file, 'w', encoding='utf-16') as file:
                def export_subkeys(key, indent=""):
                    for i in range(winreg.QueryInfoKey(key)[0]):
                        subkey_name = winreg.EnumKey(key, i)
                        subkey_path = os.path.join(hive_path, subkey_name)
                        
                        file.write(f"{indent}[{subkey_path}]\n")
                        
                        with winreg.OpenKey(key, subkey_name) as subkey:
                            export_subkeys(subkey, indent + "  ")
                
                export_subkeys(hive)

            print(f"{hive_name} hive exported to {hive_output_file}")
    except Exception as e:
        print(f"Error: {e}")

def systemInfo():
	print("\n==========System Info File==========")
	subprocess.run(['systeminfo'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, encoding='utf-8')

	output_directory = os.getcwd()
	system_info_folder = os.path.join(output_directory, "SystemInfo")
	if not os.path.exists(system_info_folder):
		os.makedirs(system_info_folder)

	try:
		system_info_output_file = os.path.join(system_info_folder, "system_info.txt")
		with open(system_info_output_file, 'w', encoding='utf-8') as file:
			file.write(subprocess.getoutput('systeminfo'))

		print(f"System info exported to {system_info_output_file}")
	except Exception as e:
		print(f"Error: {e}")


def systemAudit():
	print("\n==========System Audit Policy File==========")
	subprocess.run(['auditpol', '/get', '/category:*'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, encoding='utf-8')

	output_directory = os.getcwd()
	audit_policy_folder = os.path.join(output_directory, "AuditPolicy")
	if not os.path.exists(audit_policy_folder):
		os.makedirs(audit_policy_folder)

	try:
		audit_policy_output_file = os.path.join(audit_policy_folder, "audit_policy_info.txt")
		with open(audit_policy_output_file, 'w', encoding='utf-8') as file:
			file.write(subprocess.getoutput('auditpol /get /category:*'))

		print(f"Audit policy info exported to {audit_policy_output_file}")
	except Exception as e:
		print(f"Error: {e}")


def groupPolicy():
	print("\n==========Group Policy File==========")
	subprocess.run(['gpresult', '/R'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, encoding='utf-8')
	output_directory = os.getcwd()
	group_policy_folder = os.path.join(output_directory, "GroupPolicy")
	if not os.path.exists(group_policy_folder):
		os.makedirs(group_policy_folder)

	try:
		group_policy_output_file = os.path.join(group_policy_folder, "group_policy_info.txt")
		with open(group_policy_output_file, 'w', encoding='utf-8') as file:
			file.write(subprocess.getoutput('gpresult /R'))

		print(f"Group policy info exported to {group_policy_output_file}")
	except Exception as e:
		print(f"Error: {e}")


def eventLog():
	print("\n==========Event Viewer Log File==========")
	output_directory = os.getcwd()
	event_logs_folder = os.path.join(output_directory, "EventLogs")
	if not os.path.exists(event_logs_folder):
		os.makedirs(event_logs_folder)

	try:
        # 시스템 이벤트 로그 내용 가져오기
		system_log_output_file = os.path.join(event_logs_folder, "system_event_log.txt")
		subprocess.run(['wevtutil', 'qe', 'System', '/f:text', '/c:1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, encoding='utf-8')
		with open(system_log_output_file, 'w', encoding='utf-8') as file:
			file.write(subprocess.getoutput(f'wevtutil qe System /f:text /c:1'))

		print(f"System event log exported to {system_log_output_file}")

        # 응용 프로그램 이벤트 로그 내용 가져오기
		application_log_output_file = os.path.join(event_logs_folder, "application_event_log.txt")
		subprocess.run(['wevtutil', 'qe', 'Application', '/f:text', '/c:1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, encoding='utf-8')
		with open(application_log_output_file, 'w', encoding='utf-8') as file:
			file.write(subprocess.getoutput(f'wevtutil qe Application /f:text /c:1'))

		print(f"Application event log exported to {application_log_output_file}")
	except Exception as e:
		print(f"Error: {e}")


def serviceLog():
	print("\n==========Service Log File==========")
	output_directory = os.getcwd()
	service_log_folder = os.path.join(output_directory, "ServiceLog")
	if not os.path.exists(service_log_folder):
		os.makedirs(service_log_folder)

	try:
        # 서비스 로그를 가져와서 파일로 저장
		service_log_output_file = os.path.join(service_log_folder, "service_log.txt")
		subprocess.run(['net', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, encoding='utf-8')
		with open(service_log_output_file, 'w', encoding='utf-8') as file:
			file.write(subprocess.getoutput('net start'))

		print(f"Service log exported to {service_log_output_file}")
	except Exception as e:
		print(f"Error: {e}")


def hostsData():
	print("\n==========Hosts Data File==========")
	output_directory = os.getcwd()
	hosts_folder = os.path.join(output_directory, "Hosts")
	if not os.path.exists(hosts_folder):
		os.makedirs(hosts_folder)

	try:
		hosts_file_path = r"C:\Windows\System32\drivers\etc\hosts"  # Hosts 파일 경로
		hosts_output_file = os.path.join(hosts_folder, "hosts.txt")

		with open(hosts_file_path, 'r', encoding='utf-8') as input_file, open(hosts_output_file, 'w', encoding='utf-8') as output_file:
			hosts_content = input_file.read()
			output_file.write(hosts_content)

		print(f"Hosts file exported to {hosts_output_file}")
	except Exception as e:
		print(f"Error: {e}")


def srum():
	print("\n==========SRUM File==========")	
	output_directory = os.getcwd()
	srum_folder = os.path.join(output_directory, "SRUM")
	if not os.path.exists(srum_folder):
		os.makedirs(srum_folder)

	try:
		with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SRUM\Extensions", 0, winreg.KEY_READ) as key:
			i = 0
			while True:
				try:
					subkey_name = winreg.EnumKey(key, i)
					subkey_path = os.path.join(r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SRUM\Extensions", subkey_name)

					with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path, 0, winreg.KEY_READ) as subkey:
						j = 0
						while True:
							try:
								value_name, srum_data, _ = winreg.EnumValue(subkey, j)

                                # 각 데이터를 파일로 저장 (바이너리 모드 또는 문자열 모드로 열기)
								srum_output_file = os.path.join(srum_folder, f"{subkey_name}_{value_name}.txt")
								with open(srum_output_file, 'wb' if isinstance(srum_data, bytes) else 'w') as file:
									if isinstance(srum_data, bytes):
										file.write(srum_data)
									else:
										file.write(str(srum_data))
							
								print(f"SRUM data from {subkey_name}/{value_name} exported to {srum_output_file}")

								j += 1
							except OSError as e:
								break

					i += 1
				except OSError as e:
					break

			if i == 0:
				print("No SRUM data found.")
	except Exception as e:
		print(f"Error: {e}")


def environmentVar():
	print("\n==========Envionment Variable File==========")
	output_directory = os.getcwd()
	environ_var_folder = os.path.join(output_directory, "EnvironmentVar")
	if not os.path.exists(environ_var_folder):
		os.makedirs(environ_var_folder)

	output_file = os.path.join(environ_var_folder, "environment_variables.txt")
	try:
		with open(output_file, 'w') as file:
			for key, value in os.environ.items():
				file.write(f"{key} = {value}\n")

		print(f"Environment variables exported to {output_file}")
	except Exception as e:
		print(f"Error: {e}")


def patchList():
	print("\n==========Patch List File==========")
	output_directory = os.getcwd()
	patch_list_folder = os.path.join(output_directory, "PatchList")
	if not os.path.exists(patch_list_folder):
		os.makedirs(patch_list_folder)

	try:
		with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\Packages", 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
			i = 0
			while True:
				try:
					package_name = winreg.EnumKey(key, i)
					patch_list_file = os.path.join(patch_list_folder, f"{package_name}.txt")
                    
					with open(patch_list_file, 'w') as file:
						file.write(package_name)
                    
					i += 1
				except OSError as e:
					break

			if i > 0:
				print(f"Patch list exported to {patch_list_folder}")
			else:
				print("No patch list information found.")
	except Exception as e:
		print(f"Error: {e}")


def memoryDump():
	print("\n==========MemoryDump File==========")
	current_directory = os.path.dirname(os.path.abspath(__file__))
	destination_folder = os.path.join(current_directory, "MemoryDump")

	# "MemoryDump" 폴더 생성 후 저장
	if not os.path.exists(destination_folder):
		os.makedirs(destination_folder)
	
	# 메모리 덤프 파일 경로
	memory_dump_file = os.path.join(destination_folder, 'memory_dump.txt')

	h = hpy()
	with open(memory_dump_file, "w") as f:
		f.write(str(h.heap()))


def userAssist():
	print("\n==========UserAssist File==========")

	keys_to_copy = [
		# 실행파일 기록 subkey
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count",
		# 바로가기 실행 기록 subkey
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{F4E57C4B-2036-45F0-A9AB-443BCFE33D9F}\Count"
    ]

	current_directory = os.getcwd()
	destination_folder = os.path.join(current_directory, "UserAssist")

	if not os.path.exists(destination_folder):
		os.makedirs(destination_folder)


	try:
		with winreg.OpenKey(winreg.HKEY_CURRENT_USER, keys_to_copy[0], 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
			userAssistRegistry(key, destination_folder, 1)
		with winreg.OpenKey(winreg.HKEY_CURRENT_USER, keys_to_copy[1], 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
			userAssistRegistry(key, destination_folder, 2)
	except Exception as e:
		print(f"Error: {e}")

def sanitize_filename(filename):
    # 파일 이름에 유효하지 않은 문자를 대체
    invalid_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|', '.', '&', '!', '@', '#', '$', '%', '^', '(', ')', '[', ']', '{', '}', '+', '=', ',', ';', '`', "'", '~', ' ']
    for char in invalid_chars:
        filename = filename.replace(char, '_')

    # 파일 이름을 최대 100자로 제한
    return filename[:100]

def userAssistRegistry(subkey, output_directory, num):
	try:
		if not os.path.exists(output_directory):
			os.makedirs(output_directory)
			
		if num == 1:	
			subkey_name = str(winreg.QueryInfoKey(subkey)[0])
			subkey_path = os.path.join(output_directory, "CEBFF5CD-ACE2-4F4F-9178-9926F41749EA")
		else:
			subkey_name = str(winreg.QueryInfoKey(subkey)[0])
			subkey_path = os.path.join(output_directory, "F4E57C4B-2036-45F0-A9AB-443BCFE33D9F")

		if not os.path.exists(subkey_path):
			os.makedirs(subkey_path)

		i = 0
		while True:
			try:
				value_name, value_data, _ = winreg.EnumValue(subkey, i)
				value_output_file = os.path.join(subkey_path, f"{sanitize_filename(value_name)}.txt")

                # 중간 디렉터리가 없는 경우 생성
				value_output_dir = os.path.dirname(value_output_file)
				if not os.path.exists(value_output_dir):
					os.makedirs(value_output_dir)
                
				with open(value_output_file, 'w') as file:
					file.write(str(value_data))  # value_data를 문자열로 변환하여 쓰기
				i += 1
			except OSError as e:
				print(f"Error while processing subkey {subkey_name}: {e}")
				break

		print(f"Data from subkey {subkey_name} has been saved to {subkey_path}")
	except Exception as e:
		print(f"Error: {e}")

def autoRun():
	print("\n==========AutoRun File==========")
	output_directory = os.getcwd()
	autorun_folder = os.path.join(output_directory, "AutoRun")
	if not os.path.exists(autorun_folder):
		os.makedirs(autorun_folder)

	try:
		with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
			values = {}
			i = 0
			while True:
				try:
					value_name, value_data, _ = winreg.EnumValue(key, i)
					values[value_name] = value_data
					i += 1
				except OSError as e:
					break

			if values:
				output_file = os.path.join(autorun_folder, "autorun_values.txt")
				with open(output_file, 'w') as file:
					for name, data in values.items():
						file.write(f"{name} = {data}\n")

				print(f"AutoRun values exported to {output_file}")
			else:
				print("No AutoRun values found.")
	except Exception as e:
		print(f"Error: {e}")

def registryUser():
	print("\n==========Registry User File==========")
	output_directory = os.getcwd()
	registry_folder = os.path.join(output_directory, "AllUserRegistry")
	if not os.path.exists(registry_folder):
		os.makedirs(registry_folder)

	try:
		with winreg.ConnectRegistry(None, winreg.HKEY_USERS) as users_hive:
			with winreg.OpenKey(users_hive, None) as users_key:
				num_subkeys = winreg.QueryInfoKey(users_key)[0]
                
				for i in range(num_subkeys):
					user_sid = winreg.EnumKey(users_key, i)
					user_hive_path = f"{user_sid}\\Software"  # 사용자 하이브 경로

					with winreg.ConnectRegistry(None, winreg.HKEY_USERS) as user_hive:
						with winreg.CreateKey(user_hive, user_hive_path) as user_key:
                            # 사용자 레지스트리 정보를 파일로 저장
							user_output_file = os.path.join(registry_folder, f"{user_sid}_registry.txt")
							with open(user_output_file, 'w', encoding='utf-16') as file:
								def export_subkeys(key, indent=""):
									for j in range(winreg.QueryInfoKey(key)[0]):
										subkey_name = winreg.EnumKey(key, j)
										subkey_path = os.path.join(user_hive_path, subkey_name)

										file.write(f"{indent}[{subkey_path}]\n")

										with winreg.OpenKey(key, subkey_name) as subkey:
											export_subkeys(subkey, indent + "  ")

								export_subkeys(user_key)

							print(f"{user_sid} registry exported to {user_output_file}")
    
	except Exception as e:
		print(f"Error: {e}")


def export_registry_key(reg_file, hkey, key_path):
    try:
        key = winreg.OpenKey(hkey, key_path)
        for i in range(winreg.QueryInfoKey(key)[0]):
            sub_key_name = winreg.EnumKey(key, i)
            sub_key_path = os.path.join(key_path, sub_key_name)
            reg_file.write(f'\n[{sub_key_path}]\n')

            export_registry_key(reg_file, hkey, sub_key_path)
        
        for i in range(winreg.QueryInfoKey(key)[1]):
            value_name, value_data, value_type = winreg.EnumValue(key, i)
            if value_type == winreg.REG_SZ:
                reg_file.write(f'"{value_name}"="{value_data}"\n')
            elif value_type == winreg.REG_DWORD:
                reg_file.write(f'"{value_name}"=dword:{value_data:08X}\n')
            # 여러 다른 레지스트리 값 유형에 대한 처리 추가 가능
            
    except Exception as e:
        pass


def save_browser_history():
	print("\n==========Browser History File==========")
	current_directory = os.path.dirname(os.path.abspath(__file__))
	destination_folder = os.path.join(current_directory, "BrowserHistory")

	# "MemoryDump" 폴더 생성 후 저장
	if not os.path.exists(destination_folder):
		os.makedirs(destination_folder)

	# 크롬 브라우저의 기록 데이터베이스 경로
	chrome_history_path = os.path.expanduser('~') + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
	# 복사할 임시 파일 경로
	temp_db_path = os.path.join(destination_folder, 'temp_history')

	# 기록 데이터베이스 파일 복사
	copyfile(chrome_history_path, temp_db_path)

	# 데이터베이스 연결
	connection = sqlite3.connect(temp_db_path)
	cursor = connection.cursor()

	# 방문 기록 가져오기
	cursor.execute("SELECT title, url, last_visit_time FROM urls")
	history = cursor.fetchall()

	# 파일로 저장
	history_file_path = os.path.join(destination_folder, 'browser_history.txt')
	with open(history_file_path, 'w', encoding='utf-8') as file:
		for item in history:
			title, url, timestamp = item
			time_formatted = str(timestamp)
			file.write(f"Title: {title}\nURL: {url}\nTimestamp: {time_formatted}\n\n")

	# 연결 종료 및 임시 데이터베이스 파일 삭제
	cursor.close()
	connection.close()
	os.remove(temp_db_path)

	print("브라우저 기록이 'Browser' 폴더에 저장되었습니다.")

def recycleBin():
	print("\n==========Recycle Bin File==========")
	
	# 'RecycleBin' 폴더 생성
	destination_folder = os.path.join(os.getcwd(), 'RecycleBin')
	if not os.path.exists(destination_folder):
		os.makedirs(destination_folder)

	try:
	    # Powershell 스크립트 실행
		script_path = os.path.join(os.path.dirname(__file__), 'copy_recycle.ps1')
		command = ["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path]
		subprocess.run(command, shell=True, check=True)

		print("휴지통 내용이 'RecycleBin' 폴더에 복사되었습니다.")
	except Exception as e:
	    print(f"오류가 발생했습니다: {e}")

def lnkFile():
	print("\n==========LNK File==========")
	# LNK 폴더 생성 후 저장
	current_directory = os.path.dirname(os.path.abspath(__file__))
	destination_folder = os.path.join(current_directory, "LNK")
	if not os.path.exists(destination_folder):
		os.makedirs(destination_folder)

	# .lnk파일 위치
	source_folder = os.path.expanduser("~") + "\\AppData\\Roaming\\Microsoft\\Windows\\Recent"

	# file copy
	for root, dirs, files in os.walk(source_folder):
		for file in files:
			source_file_path = os.path.join(root, file)
			destination_file_path = os.path.join(destination_folder, file)	

			try:
				shutil.copy2(source_file_path, destination_file_path)
				print(f"복사 완료: {file}")
			except Exception as e:
				print(f"복사 실패: {file}, 오류: {e}")
			
def PowerShellLogFile():
	print("\n==========PowerShell Log File==========")
	# PowerShellLog 폴더 생성 후 저장
	current_directory = os.path.dirname(os.path.abspath(__file__))
	destination_folder = os.path.join(current_directory, "PowerShellLog")
	if not os.path.exists(destination_folder):
		os.makedirs(destination_folder)

	# .lnk파일 위치
	source_folder = os.path.expanduser("~") + "\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\PSReadLine"

	# file copy
	for root, dirs, files in os.walk(source_folder):
		for file in files:
			source_file_path = os.path.join(root, file)
			destination_file_path = os.path.join(destination_folder, file)
			try:
				shutil.copy2(source_file_path, destination_file_path)
				print(f"복사 완료: {file}")
			except Exception as e:
				print(f"복사 실패: {file}, 오류: {e}")

def main():
	init()
	while(True):	
		showOptions()
		options = input("[Select Option] : ")
		
		if options == "0":
			print("Good Bye!")
			exit()
		elif options == "1":
			memoryDump()
		elif options == "2":
			registryHive()
		elif options == "3":
			systemInfo()
		elif options == "4":
			systemAudit()
		elif options == "5":
			groupPolicy()
		elif options == "6":
			eventLog()
		elif options == "7":
			serviceLog()
		elif options == "8":
			hostsData()
		elif options == "9":
			srum()
		elif options == "10":
			environmentVar()
		elif options == "11":
			patchList()			
		elif options == "20":
			userAssist()
		elif options == "21":
			autoRun()	
		elif options == "22":
			registryUser()
		elif options == "23":
			save_browser_history()
		elif options == "24":
			recycleBin()
		elif options == "25":
			lnkFile()
		elif options == "26":
			PowerShellLogFile()
		else :
			print("\nPlease input correct options!")
			pass


if __name__ == "__main__":
	main()
