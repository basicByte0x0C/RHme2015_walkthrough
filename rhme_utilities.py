#!/usr/bin/env python

import serial, argparse

# CR+LF, needed to send commands to RHme Device
crlf = '\r\n'

# All known commands
requestNonce = "A" + crlf   # Request Nonce
requestVar = "V" + crlf     # Request Variables
requestHelp = "H" + crlf    # Request Help
userPassword = "R00063B4C"
privPassword = "R00798068"
adminPassword = "R498451D5"

# Convert int to hex value for argument parser
def hex_type(value): 
    try: 
        return int(value, 16) 
    except ValueError: 
        raise argparse.ArgumentTypeError(f"Invalid hexadecimal value: '{value}'")

# Arguments parse to customize bruteforce
parser = argparse.ArgumentParser(description="Tool for RHme 2015 hacking challenge.")
parser.add_argument('-com', type=str, help="Specify the Serial Port to be used. Default: COM3")
parser.add_argument('-baud', type=int, help="Specify the baudrate for the serial communication. Default: 1000000")

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
    print("----- Start Flushing -----")
    print("")
    while True:
        flush = serialPort.readline()
        if flush.decode() in [crlf, '', '\n']:
            print("----- Flush successful -----")
            break
        else:
            print(flush.decode())
