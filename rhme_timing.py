#!/usr/bin/env python

from rhme_utilities import *

#---------------------------------------
#   Implementation
#---------------------------------------

# Settings
pre = "00"
target = "F0"
post = "0000"

# Info and Style
print("")
print("-------------------- RHme 2015 Timing Tool --------------------")
print("")

# Define Main
def main():
    # Flush serial
    Serial_Flush()

    # Do measurements
    for byte in range(0xF, 0x0):
        # Authenticate
        # Nonce
        sendCommand = "A" + crlf
        serialPort.write(sendCommand.encode())
        temp = serialPort.readline()
        print(temp.decode())
        temp = serialPort.readline()
        temp = serialPort.readline()
        print(temp.decode())

        # Response
        sendCommand = "R" + pre + byte + post + crlf
        print(sendCommand.encode())
        serialPort.write(sendCommand.encode())
        # Flush Serial
        for f in range(0, 2):
            temp = serialPort.readline()
            print(temp.decode())
      
    print("Job's done!")

# Run Main
if __name__ == '__main__':
    main()
