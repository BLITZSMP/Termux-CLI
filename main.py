#!/data/data/com.termux/files/usr/bin/python import os import time import subprocess

def clear(): os.system("clear")

def pause(): input("\n[ Press Enter to return to menu... ]")

def boot_xfce(): os.system("proot-distro login debian -- termux-x11 :1 -xstartup 'dbus-launch --exit-with-session xfce4-session'")

def boot_cli(): os.system("proot-distro login debian")

def update_system(): os.system("apt update && apt upgrade -y")

def launch_firefox(): os.system("proot-distro login debian -- firefox")

def display_status(): os.system("neofetch || uname -a")

def main(): while True: clear() print(""" ..|'''.|
.|'     '    ...   ... ..    ....
||         .|  '|.  ||' '' .|...|| '|.      . ||   ||  ||     ||
''|....'   '|..|' .||.     '|...'

[█ Termux CLI Launcher █]

███ █ => [1] Boot DE (XFCE) [2] Boot DE CLI only [3] Update System [4] Display System Status [5] Launch Firefox (in Debian) [6] Use Termux Shell [7] Exit Termux ███ """)

choice = input("Enter choice: ").strip()

    if choice == "1":
        boot_xfce()
    elif choice == "2":
        boot_cli()
    elif choice == "3":
        update_system()
        pause()
    elif choice == "4":
        display_status()
        pause()
    elif choice == "5":
        launch_firefox()
    elif choice == "6":
        break  # Use Termux shell
    elif choice == "7":
        os.system("exit")
    else:
        print("\n[!] Invalid choice!")
        time.sleep(1)

if name == "main": main()

