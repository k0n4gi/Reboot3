import os
import sys
import pyfiglet

# 'mac_result' 폴더 생성
results_folder = 'mac_result'
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

def mac_feature1():
    print("Memory dump")
    os.system('sudo python3 Mac/memory_dump.py')  # Assuming the feature file is named "memory_dump.py"

def mac_feature2():
    print("Executing MAC Feature 2")
    os.system('sudo python3 Mac/Feature2.py')  # Assuming the feature file is named "Feature2.py"

def mac_feature3():
    print("Executing MAC Feature 3")
    os.system('sudo python3 mac/Feature3.py')  # Assuming the feature file is named "Feature3.py"

def save_to_txt():
    name = input("Enter your NAME: ")
    days = input("Enter the number of DAYS: ")
    os_type = input("Enter the OS type: ")
    
    result_file_path = os.path.join(results_folder, 'user_data.txt')
    with open(result_file_path, "a") as file:
        file.write(f"NAME: {name}\nDAYS: {days}\nOS: {os_type}\n\n")
    print("Data saved successfully!")

def mac_main():
    while True:
        reboot_ascii = pyfiglet.figlet_format("MAC", font="slant")
        box_width = max(map(len, reboot_ascii.split('\n')))
        print("┌" + "─" * (box_width + 2) + "┐")
        print("│ " + "\n│ ".join(reboot_ascii.split('\n')) + " │")
        copyright_line = "Copyright © Team Reboot"
        copyright_spacing = " " * ((box_width - len(copyright_line)) // 2)
        print("│" + copyright_spacing + copyright_line + copyright_spacing + "│")
        print("└" + "─" * (box_width + 2) + "┘")
        print("\n")
        
        print("1. Memory_dump")
        print("2. Execute MAC Feature 2")
        print("3. Execute MAC Feature 3")
        print("4. Exit and Save to txt")
        choice = input("Enter the number of the feature you want to execute: ")

        if choice == '1':
            mac_feature1()
        elif choice == '2':
            mac_feature2()
        elif choice == '3':
            mac_feature3()
        elif choice == '4':
            save_to_txt()
            print("Exiting MAC_ALL.py and returning to main menu...")
            break
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    mac_main()
