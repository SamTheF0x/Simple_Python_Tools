#!/usr/bin/python3

##############################################################
# Created by @SamTheF0x -------------------------------------#
# This script can be used, modify, replicate for any purpose #
# without any restrictions. ---------------------------------#
##############################################################

# Import required libraries

# hashlib to e able to use the hash algorythms
import hashlib
# argparse to get a help menu and options from terminal args
import argparse

#ANSI Escape sequence codes are in octal mode '[ is a control sequence introducer'
#Using a class to be able to reuse it for other color purposes (Review the usage of classes and their implementation)
class terminal_output_colors:
    yellow_color = '\033[33m'
    green_color = '\033[32m'
    reset_color = '\033[0m'
    bold_style = '\033[1m'
    red_background_color = '\033[41m'

# Create a simple script to check the hash of a file and compare it with the hash provided in order to confirm they match or there's an error with the downloaded file

# Create a help menu and the arguments to pass to create a better UI and UX

parser = argparse.ArgumentParser(
    prog='Hash Compare',
    description='This script is for verifying file integrity of any file. It can be for a file downloaded or for any copy of a file',
    epilog='With love for you SamTheF0x')
parser.add_argument('-f', '--filename', help='File to test its integrity')
parser.add_argument('-fh', '--filehash', help='hash provided by the source', type=str)
parser.add_argument('-a', '--algorythm', help='Type of hash used')
args = parser.parse_args()


# Get the file, hash and hash algorithm from the user variables got from the args menu.
filename_to_hash = args.filename
provided_hash = args.filehash
hash_type = args.algorythm

# Uppercase hash name so we can compare it in the conditions
upper_hash = hash_type.upper()

#Calculate hash of the file

#Calculate MD5 hash
if upper_hash == "MD5":
	outcome = hashlib.md5(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print(terminal_output_colors.green_color + "Everything is OK" + terminal_output_colors.reset_color)
	else:
		print(terminal_output_colors.red_background_color + "Not the same file" + terminal_output_colors.reset_color)

#Calculate SHA1 hash
if upper_hash == "SHA1":
	outcome = hashlib.sha1(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print(terminal_output_colors.green_color + "Everything is OK" + terminal_output_colors.reset_color)
	else:
		print(terminal_output_colors.red_background_color + "Not the same file" + terminal_output_colors.reset_color)

#Calculate SHA224 hash
if upper_hash == "SHA224":
	outcome = hashlib.sha224(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print(terminal_output_colors.green_color + "Everything is OK" + terminal_output_colors.reset_color)
	else:
		print(terminal_output_colors.red_background_color + "Not the same file" + terminal_output_colors.reset_color)

#Calculate SHA256 hash
if upper_hash == "SHA256":
	outcome = hashlib.sha256(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print(terminal_output_colors.green_color + "Everything is OK" + terminal_output_colors.reset_color)
	else:
		print(terminal_output_colors.red_background_color + "Not the same file" + terminal_output_colors.reset_color)

#Calculate SHA384 hash
if upper_hash == "SHA384":
	outcome = hashlib.sha384(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print(terminal_output_colors.green_color + "Everything is OK" + terminal_output_colors.reset_color)
	else:
		print(terminal_output_colors.red_background_color + "Not the same file" + terminal_output_colors.reset_color)

#Calculate SHA512 hash
if upper_hash == "SHA512":
	outcome = hashlib.sha512(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print(terminal_output_colors.green_color + "Everything is OK" + terminal_output_colors.reset_color)
	else:
		print(terminal_output_colors.red_background_color + "Not the same file" + terminal_output_colors.reset_color)
