from pyfiglet import Figlet
import LnkParse3
import os
import shutil


def init():
	f = Figlet(font='slant')
	print(f.renderText('Reboot'))
	print("This program is Artifact collecter\n")

def showOptions():
	print("==========Options==========")
	print("1) LNK File")
	print("2) PowerShell Log File")
	print("0) exit program")

def lnkFile():
	print("==========LNK File==========")
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
	print("==========PowerShell Log File==========")
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
			lnkFile()
		elif options == "2":
			PowerShellLogFile()
		else :
			print("\nPlease input correct options!")
			pass


if __name__ == "__main__":
	main()