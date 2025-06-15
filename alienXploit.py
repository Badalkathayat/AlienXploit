# AlienXploit - Intergalactic Bug Hunter Tool (v1.2)
# Author: Badal Kathayat (aka HackerFromHills)

import os
import subprocess
import time
import shutil
from termcolor import cprint, colored
from concurrent.futures import ThreadPoolExecutor

def show_banner():
    banner = """
       👽🚗 ALIENXPLOIT v1.2 - Intergalactic Bug Hunter Tool 📂

    ███▃   ███▃███▃████▃██▃   ██▃██▃  ██▃███▃
   ██╔═█║██▃     ██╔════╗██▃████▃  ██╓██▃ ═══█╔
   ██████║██▃     ████▃  ██║██▃███▃  ██║████╞ █████╓
   ██╔══█║██▃     ██╔═══╗██║██▃══█▃██╔═══╗
   ██▃  ██║███▃██║███▃██║ ═██║██▃  ██▃██║
   ╚╝  ╚╝╚╝╚╝╚╝╚╝  ╚╝╚╝  ╚╝╚╝
   -----------------------------------------------------------
       "Hunting vulnerabilities across the galaxy..." 🌌✨
    """
    cprint(banner, 'green')

def check_tools():
    tools = ['assetfinder', 'nmap', 'nuclei', 'dalfox']
    for tool in tools:
        if shutil.which(tool) is None:
            cprint(f"[!] {tool} not found! Please install before running AlienXploit.", 'red')
            exit(1)

log_file = "AlienXploit.log"
def log(msg, level="info"):
    colors = {"info": 'yellow', "success": 'green', "error": 'red', "warning": 'magenta'}
    tags = {"info": "[*]", "success": "[+]", "error": "[-]", "warning": "[!]"}
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    message = f"{timestamp} {tags[level]} {msg}"
    cprint(message, colors[level])
    with open(log_file, "a") as f:
        f.write(message + "\n")

def subdomain_enum(domain):
    log("Subdomain Enumeration Started...")
    os.makedirs(f"output/{domain}", exist_ok=True)
    os.system(f"assetfinder --subs-only {domain} > output/{domain}/subdomains.txt")
    log(f"Subdomains saved to output/{domain}/subdomains.txt", "success")

def port_scan(target):
    log("Running Nmap Scan...")
    os.makedirs(f"output/{target}", exist_ok=True)
    os.system(f"nmap -sS -Pn -T4 {target} -oN output/{target}/nmap_scan.txt")
    log(f"Scan complete. Output saved to output/{target}/nmap_scan.txt", "success")

def vuln_scan(domain):
    log("Starting Vulnerability Scan using Nuclei...")
    os.system(f"nuclei -l output/{domain}/subdomains.txt -o output/{domain}/nuclei_result.txt")
    log(f"Vulnerability Scan complete. Output in output/{domain}/nuclei_result.txt", "success")

def xss_scan(domain):
    log("Starting XSS scan using Dalfox...")
    cleaned_file = f"output/{domain}/clean_subdomains.txt"
    with open(f"output/{domain}/subdomains.txt", 'r') as infile, open(cleaned_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if line and '.' in line:
                outfile.write(line + '\n')
    os.system(f"dalfox file {cleaned_file} --output output/{domain}/dalfox_result.txt")
    log(f"XSS Scan complete. Output in output/{domain}/dalfox_result.txt", "success")

def full_scan(target):
    log("Starting full scan on target: " + target)
    os.makedirs(f"output/{target}", exist_ok=True)
    with ThreadPoolExecutor() as executor:
        executor.submit(subdomain_enum, target)
        executor.submit(port_scan, target)
        executor.submit(vuln_scan, target)
        executor.submit(xss_scan, target)
    shutil.make_archive(f"output/{target}", 'zip', f"output/{target}")
    log(f"[✓] Full Scan Complete. Results zipped as output/{target}.zip", "success")

def main():
    show_banner()
    check_tools()
    while True:
        print(colored("\n[ MENU ]", 'yellow'))
        print("[1] Subdomain Enumeration")
        print("[2] Port Scan")
        print("[3] Vulnerability Scan (Nuclei)")
        print("[4] XSS Scan (Dalfox)")
        print("[5] Run Full Scan")
        print("[6] Exit")
        choice = input(colored("\nEnter your choice: ", 'cyan'))

        if choice == '1':
            domain = input(colored("Enter domain: ", 'yellow'))
            subdomain_enum(domain)
        elif choice == '2':
            target = input(colored("Enter target IP or domain: ", 'yellow'))
            port_scan(target)
        elif choice == '3':
            domain = input(colored("Enter domain: ", 'yellow'))
            vuln_scan(domain)
        elif choice == '4':
            domain = input(colored("Enter domain: ", 'yellow'))
            xss_scan(domain)
        elif choice == '5':
            target = input(colored("Enter target domain: ", 'yellow'))
            full_scan(target)
        elif choice == '6':
            log("Exiting... Stay safe hackerfromhills 👽", "warning")
            break
        else:
            log("Invalid option. Try again!", "error")

if __name__ == '__main__':
    main()
