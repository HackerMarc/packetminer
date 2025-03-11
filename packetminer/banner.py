import os
import time

BANNER = r"""
 ██▓███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████▄▄▄█████▓ ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀▓  ██▒ ▓▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███  ▒ ▓██░ ▒░▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄░ ▓██▓ ░ ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒ ▒██▒ ░ ▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░ ▒ ░░   ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░   ░    ░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░         ░   ▒   ░        ░ ░░ ░    ░    ░      ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ 
               ░  ░░ ░      ░  ░      ░  ░               ░    ░           ░    ░  ░   ░     
                   ░                                              - Developed by @HackerMarc         
"""

def clear_screen():
    """Clears the terminal for a clean UI."""
    os.system("cls" if os.name == "nt" else "clear")

def show_loading():
    """Simulates a loading effect."""
    loading_text = "Initializing PacketMiner..."
    print(loading_text, end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

def display_banner():
    """Displays the PacketMiner banner with a clean terminal."""
    clear_screen()
    show_loading()
    print(BANNER)
    print("\n[+] Welcome to PacketMiner - Advanced PCAP Analysis Tool\n")

if __name__ == "__main__":
    display_banner()