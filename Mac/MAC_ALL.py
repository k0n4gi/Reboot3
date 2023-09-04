import os
import sys
import pyfiglet

# 'mac_result' 폴더 생성
results_folder = './Mac/mac_result'
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

def mac_feature1():
    print("Memory dump")
    os.system('sudo python3 ./Mac/memory_dump.py')  # Assuming the feature file is named "memory_dump.py"

def mac_feature2():
    print("Trash/DS_Store")
    os.system('sudo python3 ./Mac/recyclebin.py')

def mac_feature3():
    print("port_ip_arp")
    os.system('sudo python3 ./Mac/port_ip_arp.py')

def mac_feature4():
    print("open_handle")
    os.system('sudo python3 ./Mac/open_handle.py')


def mac_feature5():
    print("sys_log")
    os.system('sudo python3 ./Mac/system_log_logarchive.py')


def mac_feature6():
    print("patch_list")
    os.system('sudo python3 ./Mac/patch_list.py')


def mac_feature7():
    print("environment")
    os.system('sudo python3 ./Mac/environment.py')


def mac_feature8():
    print("service_demon")
    os.system('sudo python3 ./Mac/service_demon.py')


def mac_feature9():
    print("cron")
    os.system('sudo python3 ./Mac/cron.py')

def mac_feature10():
    print("documents")
    os.system('sudo python3 ./Mac/documents.py')

def mac_feature11():
    print("bash_zsh_log")
    os.system('sudo python3 ./Mac/bash_zsh_log.py')

def mac_feature12():
    print("property_list")
    os.system('sudo python3 ./Mac/property_list.py')

def mac_feature13():
    print("web_history")
    os.system('sudo python3 ./Mac/web_history.py') 

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
        print("2. Trash/DS_Store")
        print("3. Port_ip_arp")
        print("4. Open_handle")
        print("5. Syslog")
        print("6. Patch_list")
        print("7. Enviornment")
        print("8. Service_demon")
        print("9. Cron")
        print("10. Documents")
        print("11. bash_zsh_log")
        print("12. Propery_list")
        print("13. Web_history")

        print("0. Exit and Save to txt")

        choice = input("Enter the number of the feature you want to execute: ")

        if choice == '1':
            mac_feature1()
        elif choice == '2':
            mac_feature2()
        elif choice == '3':
            mac_feature3()
        elif choice == '4':
            mac_feature4()
        elif choice == '5':
            mac_feature5()
        elif choice == '6':
            mac_feature6()
        elif choice == '7':
            mac_feature7()
        elif choice == '8':
            mac_feature8()
        elif choice == '9':
            mac_feature9()
        elif choice == '10':
            mac_feature10()
        elif choice == '11':
            mac_feature11()
        elif choice == '12':
            mac_feature12()
        elif choice == '13':
         mac_feature13()
        # elif choice == '14':
        #     mac_feature14()
        # elif choice == '15':
        #     mac_feature15()
        # elif choice == '16':
        #     mac_feature16()
        # elif choice == '17':
        #     mac_feature17()
        # elif choice == '18':
        #     mac_feature18()
        # elif choice == '19':
        #     mac_feature19()
        elif choice == '0':
            save_to_txt()
            print("Exiting MAC_ALL.py and returning to main menu...")
            break
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    mac_main()
