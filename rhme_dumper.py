#!/usr/bin/env python

from rhme_utilities import *

#---------------------------------------
#   Implementation
#---------------------------------------

# Change this to configure the script
dumpLength = 100

# Info and Style
print("")
print("-------------------- RHme 2015 Dumper --------------------")
print("")

# Define Main
def main():
	# Flush serial
	Serial_Flush()
	
	# Reach desired state
	sendCommand = "A" + crlf
	serialPort.write(sendCommand.encode())
	temp = serialPort.readline()
	print(temp.decode())
	temp = serialPort.readline()
	temp = serialPort.readline()
	print(temp.decode())

	sendCommand = "R00063B4C" + crlf
	serialPort.write(sendCommand.encode())
	temp = serialPort.readline()
	print(temp.decode())
	temp = serialPort.readline()
	print(temp.decode())

	# Request reading
	sendCommand = "R" + crlf
	serialPort.write(sendCommand.encode())
	temp = serialPort.readline()
	print(temp.decode())

	sendCommand = "A"
	for i in range(1, dumpLength):
		sendCommand += "A"
	sendCommand += crlf
	serialPort.write(sendCommand.encode())
	temp = serialPort.readline()
	temp = serialPort.readline()
	temp = serialPort.readline()
	temp = serialPort.readline()

	# Dump everything
	dump = open(r"dumped", "wb")
	temp = serialPort.read()
	while temp not in [b'', b'\n', crlf]:
		dump.write(temp)
		#dump.write(f'{dtemp:x}')
		temp = serialPort.read()
	print("--- Memory Dumped ---")
	dump.close()
	temp = serialPort.readline()
	print(temp.decode())

	print("I work!")

# Run Main
if __name__ == '__main__':
    main()
