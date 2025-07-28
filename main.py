
import os
import subprocess
from termcolor import colored

tools = {
    "1": ("Dalfox", "dalfox"),
    "2": ("XSSPayloadGenerator", "python3 tools/xsspayloadgen/main.py"),
    "3": ("XSSFinder", "python3 tools/xssfinder/main.py"),
    "4": ("XSSFreak", "python3 tools/xssfreak/main.py"),
    "5": ("XSpear", "ruby tools/xspear/xspear.rb"),
    "6": ("XSSCon", "python3 tools/xsscon/xsscon.py"),
    "7": ("XanXSS", "python3 tools/xanxss/xanxss.py"),
    "8": ("XSSStrike", "python3 tools/xssstrike/xssstrike.py"),
    "9": ("RVuln", "python3 tools/rvuln/main.py")
}

def banner():
    print(colored("""
__  __ ____  ____     _____                          
|  \/  |  _ \|  _ \   / ____|                         
| \  / | |_) | |_) | | (___  _ __  ___ _ __ ___  ___ 
| |\/| |  __/|  _ <   \___ \| '_ \/ __| '__/ _ \/ __|
| |  | | |   | |_) |  ____) | |_) \__ \ | |  __/\__ \
|_|  |_|_|   |____/  |_____/| .__/|___/_|  \___||___/
                             | |                     
                             |_|                     
    """, "green"))
    print(colored("XSS ARMY - Made by JawStar", "yellow"))
    print(colored("Contact: jawpent9999@proton.me\n", "cyan"))

def menu():
    banner()
    print(colored("Select a tool to run:", "cyan"))
    for key in sorted(tools.keys()):
        print(colored(f"[{key}] {tools[key][0]}", "white"))
    print(colored("[0] Exit", "red"))

def run_tool(choice):
    if choice in tools:
        os.system(tools[choice][1])
    elif choice == "0":
        print(colored("Exiting...", "red"))
        exit()
    else:
        print(colored("Invalid choice. Try again.", "red"))

if __name__ == '__main__':
    while True:
        menu()
        run_tool(input(colored("\nEnter your choice: ", "yellow")))
