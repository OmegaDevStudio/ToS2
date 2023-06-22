import os
import time
import asyncio
if os.name == "nt":
    os.system("title ToS-2 Webhook System")
from System import interceptor, launch_system, setup

def main():
    
    """Main tunnel to
    script."""

    # Terminal cleaning
    os.system("cls" if os.name == "nt" else "clear")

    # ASCII and command info.
    print("""\033[35m
▄▄▄█████▓ ▒█████    ██████2
▓  ██▒ ▓▒▒██▒  ██▒▒██    ▒ 
▒ ▓██░ ▒░▒██░  ██▒░ ▓██▄   
░ ▓██▓ ░ ▒██   ██░  ▒   ██▒
  ▒██▒ ░ ░ ████▓▒░▒██████▒▒
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
    ░      ░ ▒ ▒░ ░ ░▒  ░ ░
  ░      ░ ░ ░ ▒  ░  ░  ░  
             ░ ░        ░ 
    \033[94m\n  Select Command Choice:

    \033[35m[\033[94m1\033[35m] Bombardment
    [\033[94m2\033[35m] Launch Setup
    [\033[94m3\033[35m] Interception
    [\033[94m4\033[35m] Clean
    [\033[94m5\033[35m] Exit
    """)
    # Command input.
    command = input("\033[91m  > Enter\033[33m ")
    match command:
        case "1":
            launch_system().bombard()
        case "2":
            asyncio.run(setup())
        case "3":
            interceptor.intercept()
        case "4":
            launch_system.clean()
        case "5":
            exit()
        case other:
            print("\033[91m  > Invalid selection")

    # Makes ASCII linger a bit longer.
    time.sleep(1.3)

if __name__ == "__main__":
    while True:
        main()
    