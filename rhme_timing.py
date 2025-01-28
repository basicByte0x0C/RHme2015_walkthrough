#!/usr/bin/env python

from rhme_utilities import *
import time

#---------------------------------------
#   Implementation
#---------------------------------------

# Settings
pre = ""
post = "8451D5"

# Data
deltaTime = []
maxTime = 0.0
anotherTime = 0.0
foundByte = 0x00

# Info and Style
print("")
print("-------------------- RHme 2015 Timing Tool --------------------")
print("")

# Define Main
def main():
	# Declqrations
	global maxTime
	
	# Flush serial
	Serial_Flush()

	# Do measurements
	for byte in range(0x00, 0xFF):
		# Authenticate
		# Nonce
		sendCommand = "A" + crlf
		serialPort.write(sendCommand.encode())
		temp = serialPort.readline()
		#print(temp.decode())
		temp = serialPort.readline()
		temp = serialPort.readline()
		#print(temp.decode())
		
		# Response
		sendCommand = "R" + pre + f'{byte:02x}' + post + crlf
		#print(sendCommand.encode())
		
		# Save time
		firstTime = time.time()
		
		# Send Response
		serialPort.write(sendCommand.encode())
		while True:
			temp = serialPort.read()
			if temp.decode() not in ['','\r', '\n']:
				break
		
		# Calculate time
		newTime = time.time()
		deltaTime.append(newTime - firstTime)
		print("R" + pre + f'{byte:02x}' + post + " time: " + str(deltaTime[byte]))

		# Check Maximum time
		if maxTime < deltaTime[byte]:
			maxTime = deltaTime[byte]
			foundByte = byte

		# Check for login
		if temp.decode() != 'E':
			print("----- Logged in successfully! -----")
			print(" :: Password = " + "R" + pre + f'{byte:02x}' + post)
			break
			
	print("-- Maximum time is " + str(maxTime) + " for byte " + f'{foundByte:02x}' + " --")
	print("Job's done!")	

# Run Main
if __name__ == '__main__':
    main()
