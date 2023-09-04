import os
import sys
import pyfiglet

def feature1():
    print("Feature 1: MAC")
    os.system('sudo python3 mac/MAC_ALL.py')

def feature2():
    print("Feature 2: WINDOWS")
    os.system('sudo python3 windows/protocol_over.py')

def feature3():
    print("Feature 3: LINUX")
    os.system('sudo python3 linux/protocol_over.py')

def main():
    while True:
        reboot_ascii = pyfiglet.figlet_format("Team Reboot", font="slant")
        box_width = max(map(len, reboot_ascii.split('\n')))
        print("┌" + "─" * (box_width + 2) + "┐")
        print("│ " + "\n│ ".join(reboot_ascii.split('\n')) + " │")
        copyright_line = "Copyright © Team Reboot"
        copyright_spacing = " " * ((box_width - len(copyright_line)) // 2)
        print("│" + copyright_spacing + copyright_line + copyright_spacing + "│")
        print("└" + "─" * (box_width + 2) + "┘")
        print("\n")
        
        print("1. MAC")
        print("2. WINDOWS")
        print("3. LINUX")
        print("4. Exit")
        choice = input("Enter the number of the feature you want to execute: ")

        if choice == '1':
            feature1()
        elif choice == '2':
            feature2()
        elif choice == '3':
            feature3()
        elif choice == '4':
            print("Exiting the program...")
            sys.exit()
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()
