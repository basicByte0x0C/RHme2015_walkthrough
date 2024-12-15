#!/usr/bin/env python

import serial, argparse

# CR+LF, needed to send commands to RHme Device
crlf = '\r\n'

# Request Nonce command
requestNonce = "A" + crlf   # Request Nonce

# Convert int to hex value for argument parser
def hex_type(value): 
    try: 
        return int(value, 16) 
    except ValueError: 
        raise argparse.ArgumentTypeError(f"Invalid hexadecimal value: '{value}'")

#---------------------------------------
#   Implementation
#---------------------------------------

# Info and Style
print("")
print("-------------------- RHme 2015 Bruteforcer --------------------")
print("")

# Define Main
def main():
    # Arguments parse to customize bruteforce
    parser = argparse.ArgumentParser(description="Bruteforcer for RHme 2015 hacking challenge.")
    parser.add_argument('-com', type=str, help="Specify the Serial Port to be used.")
    parser.add_argument('-baud', type=int, help="Specify the baudrate for the serial communication.")
    parser.add_argument('-begin', type=hex_type, help="Specify the starting value of the brutforce.")
    parser.add_argument('-end', type=hex_type, help="Specify the ending value of the brutforce.")

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

    # Starting Point Argument
    if args.begin:
        startingPoint = args.begin
    else:
        startingPoint = 0x00
    print("-- Set Starting Value : " + f'{startingPoint:08x}')

    # Ending Point Argument
    if args.end:
        endingPoint = args.end
    else:
        endingPoint = 0xFFFFFFFF
    print("-- Set Ending Value : " + f'{endingPoint:08x}')

    # Serial interface
    serialPort = serial.Serial(
        port=comPort, baudrate=comBaudrate, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
    )
    
    # Flush Serial data
    print("")
    print("----- Start Flushing -----")
    print("")
    while True:
        flush = serialPort.readline()
        if flush.decode() == '\r\n':
            print("----- Flush successful -----")
            break
        else:
            print(flush.decode())

    print("")
    print("----- Begin Bruteforce -----")
    # Bruteforce the User Password
    for rspNumber in range(startingPoint, endingPoint):
        # Request Nonce
        serialPort.write(requestNonce.encode())
        temp = serialPort.readline() # Needed to flush the response

        # Read Response; Assume Nonce is the same everytime, because the RNG pin is shorted to GND
        temp = serialPort.readline()
        print("DEBUG: Received Nonce Message = " + temp.decode()) # Debug to see if response is correct
        temp = serialPort.readline() # Needed to flush the response

        # Respond with bruteforced number
        responseCommand = 'R' + f'{rspNumber:08x}' + crlf # Response in format Rxxxxxxxx
        serialPort.write(responseCommand.encode())
        print("DEBUG: Bruteforced command = " + responseCommand) # Debug to see if the response command is correct

        # Wait for the response
        while True:
            temp = serialPort.read()
            if temp.decode() not in ['','\r', '\n']:
                break
        print("DEBUG: Bruteforce result = " + temp.decode()) # Debug to see the actual response being received
        
        # Check if number was correct
        if temp.decode() != 'E':
            # Number was correct, print it
            print("----- Success! -----")
            print("")
            print("-- Result is : ")
            print(temp.decode() + serialPort.readline().decode())
            print("")
            print("-- Password is : ")
            print(hex(rspNumber))
            break

# Run Main
if __name__ == '__main__':
    main()