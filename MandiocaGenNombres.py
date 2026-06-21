#!/usr/bin/env python3
import os
import time
import random

USE_COLOR = bool(os.environ.get("TERM"))
GREEN = "\033[1;92m" if USE_COLOR else ""
RED = "\033[1;91m" if USE_COLOR else ""
VIOLET = "\033[1;95m" if USE_COLOR else ""
CYAN = "\033[1;96m" if USE_COLOR else ""
YELLOW = "\033[1;93m" if USE_COLOR else ""
WHITE = "\033[1;97m" if USE_COLOR else ""
NC = "\033[0m" if USE_COLOR else ""

BASE_DIR = "/storage/emulated/0/MandiocaNombres"
try:
    os.makedirs(BASE_DIR, exist_ok=True)
except OSError:
    BASE_DIR = "/storage/emulated/0/Download"
    try:
        os.makedirs(BASE_DIR, exist_ok=True)
    except OSError:
        BASE_DIR = os.path.expanduser("~/ciberlab_combo")
        os.makedirs(BASE_DIR, exist_ok=True)

NOMBRES = [
    "juan", "pedro", "mateo", "lucas", "diego", "thiago", "adrian", "carlos",
    "miguel", "angel", "sofia", "lucia", "valeria", "camila", "maria", "paula",
    "elena", "florencia", "daniela", "carla", "martin", "bruno", "david", "samuel",
    "leonel", "andres", "julian", "nicolas", "emilia", "renata", "bianca", "abril"
]
MAX_COMBINATIONS = 50000


def clear():
    if os.environ.get("TERM"):
        os.system("clear")
    else:
        print("\n" * 3)


def line():
    print(f"{VIOLET}" + "=" * 72 + f"{NC}")


def banner():
    clear()
    line()
    print(f"{GREEN}Mandioc Security{NC}")
    print(f"{CYAN}Local synthetic generator name:name{NC}")
    print(f"{WHITE}Ready for python and python3 on Termux{NC}")
    print(f"{WHITE}Auto save path: {BASE_DIR}{NC}")
    print(f"{WHITE}Capacity: up to {MAX_COMBINATIONS} lines{NC}")
    line()
    print()


def features():
    print(f"{CYAN}SCRIPT FEATURES{NC}")
    print(f"{GREEN}- {NC}Random names from internal list")
    print(f"{GREEN}- {NC}Format type name:name")
    print(f"{GREEN}- {NC}Option name + number")
    print(f"{GREEN}- {NC}Supports up to 50000 lines")
    print(f"{GREEN}- {NC}Repeated names allowed with stepped numbering")
    print(f"{GREEN}- {NC}Lowercase, uppercase or title")
    print(f"{GREEN}- {NC}Auto save in .txt")
    print()


def pause():
    input(f"{YELLOW}Press ENTER to continue...{NC}")


def loading(count):
    print(f"{CYAN}Generating {count} lines{NC}", end="", flush=True)
    for _ in range(4):
        time.sleep(0.12)
        print(".", end="", flush=True)
    print("\n")


def apply_format(text, mode):
    if mode == "1":
        return text.lower()
    if mode == "2":
        return text.upper()
    if mode == "3":
        return text.title()
    return text


def choose_format():
    print(f"{VIOLET}Select text format:{NC}")
    print(f"{GREEN}[1]{NC} Lowercase -> juan")
    print(f"{RED}[2]{NC} Uppercase -> JUAN")
    print(f"{CYAN}[3]{NC} Title     -> Juan")
    print()
    mode = input(f"{WHITE}Option: {NC}").strip()
    if mode not in ["1", "2", "3"]:
        print(f"{RED}[!] Invalid option. Using lowercase.{NC}")
        mode = "1"
    return mode


def ask_count(label, max_value):
    value = input(label).strip()
    if not value.isdigit():
        return None
    count = int(value)
    if count < 1 or count > max_value:
        return None
    return count


def save_file(filename, lines):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        for line_text in lines:
            f.write(line_text + "\n")
    return path


def build_name(index, mode_format, with_numbers=False, start=1):
    total_names = len(NOMBRES)
    base_name = NOMBRES[index % total_names]
    base_name = apply_format(base_name, mode_format)

    if with_numbers:
        number = start + index
        return f"{base_name}{number}"

    cycle_number = (index // total_names) + 1
    if cycle_number == 1:
        return base_name
    return f"{base_name}{cycle_number}"


def generate_lines(count, mode_format, with_numbers=False, start=1, shuffle_output=True):
    lines = []
    for i in range(count):
        name = build_name(i, mode_format, with_numbers=with_numbers, start=start)
        lines.append(f"{name}:{name}")
    if shuffle_output and count <= 10000:
        random.shuffle(lines)
    return lines


def simple_mode():
    banner()
    print(f"{VIOLET}[1] Simple random generation{NC}\n")
    count = ask_count(f"{WHITE}Line count (1-{MAX_COMBINATIONS}): {NC}", MAX_COMBINATIONS)
    filename = input(f"{WHITE}File name (ex. random.txt): {NC}").strip()
    print()
    mode = choose_format()

    if count is None or not filename:
        print(f"{RED}[!] Invalid data. Use 1 to {MAX_COMBINATIONS} lines.{NC}")
        pause()
        return

    loading(count)
    lines = generate_lines(count, mode_format=mode, with_numbers=False)
    path = save_file(filename, lines)

    print(f"{GREEN}[+] File created:{NC} {WHITE}{path}{NC}")
    print(f"{CYAN}Generated lines:{NC} {count}")
    print(f"{CYAN}Preview:{NC}")
    for line_text in lines[:15]:
        print(f" {WHITE}{line_text}{NC}")
    pause()


def name_number_mode():
    banner()
    print(f"{VIOLET}[2] Name + number generation{NC}\n")
    count = ask_count(f"{WHITE}Line count (1-{MAX_COMBINATIONS}): {NC}", MAX_COMBINATIONS)
    start_raw = input(f"{WHITE}Start number: {NC}").strip()
    filename = input(f"{WHITE}File name (ex. name_num.txt): {NC}").strip()
    print()
    mode = choose_format()

    if count is None or not start_raw.isdigit() or not filename:
        print(f"{RED}[!] Invalid data. Use 1 to {MAX_COMBINATIONS} lines.{NC}")
        pause()
        return

    start = int(start_raw)
    loading(count)
    lines = generate_lines(count, mode_format=mode, with_numbers=True, start=start)
    path = save_file(filename, lines)

    print(f"{GREEN}[+] File created:{NC} {WHITE}{path}{NC}")
    print(f"{CYAN}Generated lines:{NC} {count}")
    print(f"{CYAN}Preview:{NC}")
    for line_text in lines[:15]:
        print(f" {WHITE}{line_text}{NC}")
    pause()


def mixed_mode():
    banner()
    print(f"{VIOLET}[3] Mixed PRO generation{NC}\n")
    count = ask_count(f"{WHITE}Total line count (1-{MAX_COMBINATIONS}): {NC}", MAX_COMBINATIONS)
    filename = input(f"{WHITE}File name (ex. mixed.txt): {NC}").strip()
    print()
    mode = choose_format()

    if count is None or not filename:
        print(f"{RED}[!] Invalid data. Use 1 to {MAX_COMBINATIONS} lines.{NC}")
        pause()
        return

    loading(count)
    half = count // 2
    rest = count - half
    simple_lines = generate_lines(half, mode_format=mode, with_numbers=False)
    number_lines = generate_lines(rest, mode_format=mode, with_numbers=True, start=1)
    lines = simple_lines + number_lines
    if len(lines) <= 10000:
        random.shuffle(lines)
    path = save_file(filename, lines)

    print(f"{GREEN}[+] File created:{NC} {WHITE}{path}{NC}")
    print(f"{CYAN}Generated lines:{NC} {len(lines)}")
    print(f"{CYAN}Preview:{NC}")
    for line_text in lines[:20]:
        print(f" {WHITE}{line_text}{NC}")
    pause()


def view_files():
    banner()
    print(f"{VIOLET}[4] Generated files{NC}\n")
    files = sorted(os.listdir(BASE_DIR))
    if not files:
        print(f"{RED}No files yet.{NC}")
    else:
        for item in files:
            print(f"{WHITE}- {item}{NC}")
    pause()


def info_panel():
    banner()
    print(f"{CYAN}INFO PANEL{NC}\n")
    print(f"{GREEN}- {NC}Local synthetic generation")
    print(f"{GREEN}- {NC}Supports up to 50000 lines")
    print(f"{GREEN}- {NC}Repeated names allowed")
    print(f"{GREEN}- {NC}Stepped numbering for scale")
    print(f"{GREEN}- {NC}Run: python mandioc_security_termux_fixed.py")
    print(f"{GREEN}- {NC}Run: python3 mandioc_security_termux_fixed.py")
    pause()


def menu():
    while True:
        banner()
        features()
        print(f"{GREEN}[1]{NC} Simple random generation")
        print(f"{RED}[2]{NC} Name + number generation")
        print(f"{VIOLET}[3]{NC} Mixed PRO generation")
        print(f"{CYAN}[4]{NC} View generated files")
        print(f"{WHITE}[5]{NC} Info panel")
        print(f"{YELLOW}[0]{NC} Exit\n")

        op = input(f"{WHITE}Select option: {NC}").strip()

        if op == "1":
            simple_mode()
        elif op == "2":
            name_number_mode()
        elif op == "3":
            mixed_mode()
        elif op == "4":
            view_files()
        elif op == "5":
            info_panel()
        elif op == "0":
            print(f"{RED}Exiting...{NC}")
            break
        else:
            print(f"{RED}[!] Invalid option.{NC}")
            time.sleep(1)


if __name__ == "__main__":
    menu()
