#!/usr/bin/env python

import serial, argparse

# CR+LF, needed to send commands to RHme Device
crlf = '\r\n'

# All known commands
requestNonce = "A" + crlf   # Request Nonce
requestVar = "V" + crlf     # Request Variables
requestHelp = "H" + crlf    # Request Help

# Arguments parse to customize bruteforce
parser = argparse.ArgumentParser(description="Tool for RHme 2015 hacking challenge.")
parser.add_argument('-com', type=str, help="Specify the Serial Port to be used.")
parser.add_argument('-baud', type=int, help="Specify the baudrate for the serial communication.")

# Get Arguments
args = parser.parse_args()

# COM Argument
if args.com:
    comPort = args.com
else:
    comPort = "COM3"
print("-- Set COM Port : " + comPort)

# Baudrate Argument
if args.baud:
    comBaudrate = args.baud
else:
    comBaudrate = 1000000
print("-- Set Baudrate : " + f'{comBaudrate}')

# Serial interface
serialPort = serial.Serial(
    port=comPort, baudrate=comBaudrate, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)

# Flush Serial Interface
def Serial_Flush():
    # Flush Serial data
    print("")
    print("----- Start Initial Flushing -----")
    print("")
    while True:
        flush = serialPort.readline()
        if flush.decode() == crlf:
            print("----- Flush successfull -----")
            break
        else:
            print(flush.decode())
