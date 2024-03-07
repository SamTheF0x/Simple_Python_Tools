#!/usr/bin/python3

# Import required libraries
import hashlib

# Create a simple script to check the hash of a file and compare it with the hash provided in order to confirm they match or there's an error with the downloaded file

# Get the file, hash and hash algorithm from the user
filename_to_hash = input("Filename: ")
provided_hash = input("Hash: ")
hash_type = input("hash algorithm: ")

# Uppercase hash name so we can compare it in the conditions
upper_hash = hash_type.upper()

#Calculate hash of the file

#Calculate MD5 hash
if upper_hash == "MD5":
	outcome = hashlib.md5(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print("Everything is OK")
	else:
		print("Not the same file")

#Calculate SHA1 hash
if upper_hash == "SHA1":
	outcome = hashlib.sha1(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print("Everything is OK")
	else:
		print("Not the same file")

#Calculate SHA224 hash
if upper_hash == "SHA224":
	outcome = hashlib.sha224(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print("Everything is OK")
	else:
		print("Not the same file")

#Calculate SHA256 hash
if upper_hash == "SHA256":
	outcome = hashlib.sha256(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print("Everything is OK")
	else:
		print("Not the same file")

#Calculate SHA384 hash
if upper_hash == "SHA384":
	outcome = hashlib.sha384(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print("Everything is OK")
	else:
		print("Not the same file")

#Calculate SHA512 hash
if upper_hash == "SHA512":
	outcome = hashlib.sha512(open(filename_to_hash, 'rb').read()).hexdigest()
	print(outcome)
	print (provided_hash)
	if outcome == provided_hash:
		print("Everything is OK")
	else:
		print("Not the same file")