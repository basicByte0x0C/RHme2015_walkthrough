#!/usr/bin/env python

from rhme_utilities import *

#---------------------------------------
#   Implementation
#---------------------------------------

# Info and Style
print("")
print("-------------------- RHme 2015 Unsigned Int Dumper --------------------")
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
	# Flush Serial
	for i in range(1, 8):
		temp = serialPort.readline()
		print(temp.decode())

	# Dump everything
	dump = open(r"dump-uint", "wb")
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
