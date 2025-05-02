import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("================================")
    print("       Python Calculator        ")
    print("================================")
