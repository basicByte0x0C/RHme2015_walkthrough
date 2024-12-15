#!/usr/bin/env python

import serial, argparse

# CR+LF, needed to send commands to RHme Device
crlf = '\r\n'

# All known commands
requestNonce = "A" + crlf   # Request Nonce
requestVar = "V" + crlf     # Request Variables
requestHelp = "H" + crlf    # Request Help

# Arguments parse to customize bruteforce
parser = argparse.ArgumentParser(description="Fuzzer for RHme 2015 hacking challenge.")
parser.add_argument('-com', type=str, help="Specify the Serial Port to be used.")
parser.add_argument('-baud', type=int, help="Specify the baudrate for the serial communication.")

# Get Arguments
args = parser.parse_args()

# COM Argument
if args.com:
    comPort = args.com
else:
    comPort = "COM4"
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

#---------------------------------------
#   Implementation
#---------------------------------------

# Info and Style
print("")
print("-------------------- RHme 2015 Fuzzer --------------------")
print("")

# Fuzz Custom Range
def Fuzz_Range(range):
    print("")

    # Start by going thtough all lowercase letters
    for command in range('a', 'z'):
        # Prepare command
        #print("DEBUG: Fuzzing Command : " + command) # Debug to see what command is being tested
        command += crlf

        # Send the command
        serialPort.write(command.encode())
        temp = serialPort.readline() # Needed to flush the response

        # Read response
        temp = serialPort.readline()
        #print("DEBUG: Received Response Message = " + temp.decode()) # Debug to see if response is correct
        # Check if the Response is unexpected --> Expected response for invalid command : <bla_bla>
        if temp.decode() :
            # New command discovered
            print("-- Success --")
            print("Hidden Command : " + command)
        temp = serialPort.readline() # Needed to flush the response

# Define Main
def main():
    # Start Fuzzing
    Serial_Flush()
    print("----- Begin Fuzzing -----")

    # Fuzz lowercases
    Fuzz_Range(range('a', 'z'))
    
    # Fuzz Uppercases
    Fuzz_Range(range('A', 'Z'))

    # Fuzz Numbers
    Fuzz_Range(range(0, 100))

# Run Main
if __name__ == '__main__':
    main()