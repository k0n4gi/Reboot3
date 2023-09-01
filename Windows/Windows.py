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

def init():
	f = Figlet(font='slant')
	print(f.renderText('Reboot'))
	print("This program is Artifact collecter\n")

def showOptions():
	print("\n==========Options==========")
	print("1) Memory Dump")
	print("20) UserAssist")
	print("22) Registry")
	print("23) Internet Browser History")
	print("24) Recycle Bin")
	print("25) LNK File")
	print("26) PowerShell Log File")
	print("0) exit program")

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
	output_folder = os.path.join(os.getcwd(), "UserAssist")
	userassist_key_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist"

	# "MemoryDump" 폴더 생성 후 저장
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	try:
		with winreg.OpenKey(winreg.HKEY_CURRENT_USER, userassist_key_path, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
			userAssistsRegistry(key, output_folder)
			print(f"UserAssist data has been saved to {output_folder}")
	except Exception as e:
		print(f"Error: {e}")


def userAssistsRegistry(output_folder, registry_key):
    try:
        with open(output_folder, 'w') as file:
            subkey_count, _, _ = winreg.QueryInfoKey(registry_key)
            for i in range(subkey_count):
                subkey_name = winreg.EnumKey(registry_key, i)
                subkey_path = f"{output_folder}_{subkey_name}.txt"
                subkey = winreg.OpenKey(registry_key, subkey_name)
                file.write(f"Subkey: {subkey_name}\n")
                subkey_count, _, _ = winreg.QueryInfoKey(subkey)
                for j in range(subkey_count):
                    value_name, value_data, _ = winreg.EnumValue(subkey, j)
                    file.write(f"  {value_name}: {value_data}\n")
                file.write("\n")
                userAssistsRegistry(subkey, subkey_path)
    except Exception as e:
        print(f"Error: {e}")

def registry():
	print("\n==========Registry File==========")
	current_directory = os.path.dirname(os.path.abspath(__file__))
	destination_folder = os.path.join(current_directory, "Registry")

	# "MemoryDump" 폴더 생성 후 저장
	if not os.path.exists(destination_folder):
		os.makedirs(destination_folder)
        # 레지스트리 키 및 값 읽어오기
	with open(os.path.join(destination_folder, 'full_registry_backup.reg'), 'w', encoding='utf-16') as reg_file:
		reg_file.write('Windows Registry Editor Version 5.00\n\n')
		export_registry_key(reg_file, winreg.HKEY_LOCAL_MACHINE, '')


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
		elif options == "20":
			userAssist()
		elif options == "22":
			registry()
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
