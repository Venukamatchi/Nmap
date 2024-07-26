#!/usr/bin/python3

import nmap
from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)

# 3D and colorful ASCII Art for the VEXMAN banner
banner = f"""
{Fore.RED}{Style.BRIGHT}                                      
██╗   ██╗███████╗██╗  ██╗███╗   ███╗ █████╗ ███╗   ██╗
██║   ██║██╔════╝╚██╗██╔╝████╗ ████║██╔══██╗████╗  ██║
██║   ██║█████╗   ╚███╔╝ ██╔████╔██║███████║██╔██╗ ██║
╚██╗ ██╔╝██╔══╝   ██╔██╗ ██║╚██╔╝██║██╔══██║██║╚██╗██║
 ╚████╔╝ ███████╗██╔╝ ██╗██║ ╚═╝ ██║██║  ██║██║ ╚████║
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                      
"""

# Print the VEXMAN banner
print(banner)
print(f"{Fore.CYAN}Welcome to the VEXMAN Nmap tool!!{Style.RESET_ALL}")
print("_")

# Initialize the Nmap scanner
scanner = nmap.PortScanner()

# Prompt the user to input the IP address to scan
ip_addr = input(f"{Fore.YELLOW}Please enter the IP Address to Scan: {Style.RESET_ALL}")
print(f"The IP entered is: {Fore.GREEN}{ip_addr}{Style.RESET_ALL}")

# Prompt the user to select the type of scan
resp = input(f"""{Fore.YELLOW}\nPlease Enter the Type of Scan you wish to perform:{Style.RESET_ALL}
    {Fore.BLUE}1. SYN Scan{Style.RESET_ALL}
    {Fore.BLUE}2. UDP Scan{Style.RESET_ALL}
    {Fore.BLUE}3. TCP Connect Scan{Style.RESET_ALL}
    {Fore.BLUE}4. SCTP INIT scan{Style.RESET_ALL}
    {Fore.BLUE}5. TCP ACK scan{Style.RESET_ALL}
    {Fore.BLUE}6. TCP Null Scan{Style.RESET_ALL}
    {Fore.BLUE}7. Comprehensive Scan{Style.RESET_ALL}\n""")

print(f"You have Selected: {Fore.GREEN}{resp}{Style.RESET_ALL}")

# Dictionary to store scan options
resp_dict = {
    '1': '-sS -sV -vv',  # SYN Scan
    '2': '-sU -sV -vv',  # UDP Scan
    '3': '-sT -sV -vv',  # TCP Connect Scan
    '4': '-sY -sV -vv',  # SCTP INIT scan
    '5': '-sA -sV -vv',  # TCP ACK scan
    '6': '-sN -sV -vv',  # TCP Null Scan
    '7': '-sS -sV -O -A -sC -vv'  # Comprehensive Scan
}

# Perform the selected scan
if resp not in resp_dict.keys():
    print(f"{Fore.RED}Please enter a Valid Option!{Style.RESET_ALL}")
else:
    try:
        print(f"Nmap Version: {Fore.GREEN}{scanner.nmap_version()}{Style.RESET_ALL}")
        scanner.scan(ip_addr, "1-1024", resp_dict[resp])
        
        # Print the scanning results
        if scanner[ip_addr].state() == 'up':
            print(f"\n{Fore.GREEN}Host is up, scanning results:{Style.RESET_ALL}")
            
            for proto in scanner[ip_addr].all_protocols():
                print(f"\n{Fore.CYAN}Protocol: {proto}{Style.RESET_ALL}")
                print(f"Open Ports: {', '.join(map(str, scanner[ip_addr][proto].keys()))}")
                
                for port, info in scanner[ip_addr][proto].items():
                    print(f"\n{Fore.YELLOW}Port: {port}{Style.RESET_ALL}")
                    print(f"Service: {info['name']}")
                    print(f"State: {info['state']}")
        else:
            print(f"\n{Fore.RED}Host is down.{Style.RESET_ALL}")

    except nmap.PortScannerError as e:
        print(f"{Fore.RED}Nmap scan error: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please ensure you have Nmap installed and try using only one scan option at a time.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
