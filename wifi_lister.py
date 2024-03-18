#!/usr/bin/python3

##############################################################
# Created by @SamTheF0x -------------------------------------#
# This script can be used, modify, replicate for any purpose #
# without any restrictions. ---------------------------------#
##############################################################

# Import required libraries
# The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module intends to replace several older modules and functions:
import subprocess
# Access to underlying platform’s identifying data (Identifying OS)
import platform
# argparse to get a help menu
import argparse

# ANSI Escape sequence codes are in octal mode '[ is a control sequence introducer'
# Using a class to be able to reuse it for other color purposes (Review the usage of classes and their implementation)
# To ne used as I don't still know how to color the ouput
class terminal_output_colors:
    yellow_color = '\033[33m'
    green_color = '\033[32m'
    reset_color = '\033[0m'
    bold_style = '\033[1m'
    red_background_color = '\033[41m'

# Create a help menu and the arguments to pass to create a better UI and UX
parser = argparse.ArgumentParser(
    prog='Wifi Lister',
    description='"WiFi Lister" Python script enumerates available WiFi networks on Windows and Linux systems. It detects the OS, retrieves SSID info using platform-specific commands, and displays it for the user. Mac support forthcoming.',
    epilog='With love for you @SamTheF0x')
args = parser.parse_args()

# Get the OS of the endpoint
os_type = platform.system()
print(os_type)

# Create a function that, depending on the OS run the command to list all networks
def list_networks(os_type):
	if os_type == "Linux":
		# create variable for network command
		linux_network_commands = 'nmcli device wifi list'
		# Using the check_output() for having the network term retrieval
		# Create a list for check_output
		devices = subprocess.check_output(linux_network_commands, shell=True, text=True)
		print(devices)
	elif os_type == 'Windows':
		# create variable for network command
		windows_network_commands = 'netsh wlan show networks'
		# Using the check_output() for having the network term retrieval
		# Create a list for check_output
		devices = subprocess.check_output(linux_network_commands, shell=True, text=True)
		print(devices)
	else:
		print('Unknown OS')

# Start the program with best practices in mind
if __name__ == "__main__":
	list_networks(os_type)