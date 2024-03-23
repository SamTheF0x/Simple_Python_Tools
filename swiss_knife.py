#!/usr/bin/python3

##############################################################
# Created by @SamTheF0x -------------------------------------#
# This script can be used, modify, replicate for any purpose #
# without any restrictions. ---------------------------------#
##############################################################

# Import required libraries
# Import argparse to get the arguments from the terminal instead of input or fixed
import argparse
# Get date and time for printing formats
from datetime import datetime
# Import socket to attempt connections with other systems
import socket
# Import OS to perform the ping scans
import os

# ANSI Escape sequence codes are in octal mode '[ is a control sequence introducer'
# Using a class to be able to reuse it for other color purposes (Review the usage of classes and their implementation)
class terminal_output_colors:
    yellow_color = '\033[33m'
    green_color = '\033[32m'
    reset_color = '\033[0m'
    bold_style = '\033[1m'
    red_background_color = '\033[41m'

# Create a help menu and the arguments to pass to create a better UI and UX
parser = argparse.ArgumentParser(
    prog='Swiss Kinfe',
    description='Script will first perform a ping scan to know if the target host is up, if they are it will perform a port scan; otherwise it will exit when acknowledging that the target host is down. For the time being it scans all 65535 ports',
    epilog='With love for you SamTheF0x')
parser.add_argument('-t', '--ipaddress', help='File to test its integrity')
args = parser.parse_args()

# Get the file, hash and hash algorithm from the user variables got from the args menu.
ip_address = args.ipaddress

# Function to perform a TCP port scan (add the option to add more IPs and select ports to scan and the option to select it using the terminal as a flag)
def ping_scan(ips):
    # Create a sweet output with the target IP and port
    print(terminal_output_colors.bold_style + 'Ping Scan' + terminal_output_colors.reset_color)
    print(terminal_output_colors.green_color + '-' * 50)
    print('scanning:' + ip_address)
    print('Scan started at: ' + str(datetime.now()))
    print('-' * 50 +'\n' + terminal_output_colors.reset_color)

    # Logic to perform the ping scan to verify if a host is alive
    hostname = ip_address
    command = 'ping ' + hostname + ' -c 2 1>/dev/null'
    returned_value = os.system(command)
    if returned_value == 0:
        print(terminal_output_colors.yellow_color + hostname + ' is up' + terminal_output_colors.reset_color + '\n')
    else:
        print(terminal_output_colors.yellow_color + hostname + ' is down' + terminal_output_colors.reset_color + '\n')
        exit()

# Function to perform a TCP port scan (add the option to add more IPs and select ports to scan and the option to select it using the terminal as a flag)
def port_Scan(ips):
    # Create a sweet output with the target IP and port
    print(terminal_output_colors.bold_style + 'TCP Port Scan' + terminal_output_colors.reset_color)
    print(terminal_output_colors.green_color + '-' * 50)
    print('scanning:' + ip_address)
    print('Scan started at: ' + str(datetime.now()))
    print('-' * 50 +'\n' + terminal_output_colors.reset_color)

    # Logic to scan ports (Turn it into a function)
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # Return closed port indicator
        result = s.connect_ex((ip_address, port))
        if result == 0:
            print(terminal_output_colors.yellow_color + 'Port {} is open'.format(port) + terminal_output_colors.reset_color)
        s.close()

# Start the functions (add options to select which one(s) to pick)
ping_scan(ip_address)
port_Scan(ip_address)