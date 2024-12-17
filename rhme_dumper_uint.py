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
	sendCommand = "V" + crlf
	serialPort.write(sendCommand.encode())
	temp = serialPort.readline()
	print(temp.decode())
	temp = serialPort.readline()
	temp = serialPort.readline()
	print(temp.decode())

	# Request reading
	sendCommand = "-1" + crlf
	serialPort.write(sendCommand.encode())
	temp = serialPort.readline()
	print(temp.decode())

	# Dump everything
	dump = open(r"dumped-uint", "wb")
	temp = serialPort.read()
	while temp not in [b'', b'\n', crlf]:
		dump.write(temp)
		temp = serialPort.read()
	print("--- Memory Dumped ---")
	dump.close()
	temp = serialPort.readline()
	print(temp.decode())

	print("I work!")

# Run Main
if __name__ == '__main__':
    main()
