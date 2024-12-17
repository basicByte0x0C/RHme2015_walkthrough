#!/usr/bin/env python

from rhme_utilities import *

#---------------------------------------
#   Implementation
#---------------------------------------

# Info and Style
print("")
print("-------------------- RHme 2015 Fuzzer --------------------")
print("")

# Fuzz Custom Range
def Fuzz_Range(start, end):
    print("")

    # Start by going thtough all lowercase letters
    for command in range(ord(start),ord(end)):
        # Prepare command
        #print("DEBUG: Fuzzing Command : " + command) # Debug to see what command is being tested
        sendCommand = chr(command) + crlf

        # Send the command
        serialPort.write(sendCommand.encode())
        temp = serialPort.readline() # Needed to flush the response

        # Read response
        temp = serialPort.readline()
        print("DEBUG: Received Response Message = " + temp.decode()) # Debug to see if response is correct

        # Check if the Response is unexpected --> Expected response for invalid command : ?? Command <bla_bla> is invalid
        if "Command " + chr(command) + " is invalid" not in temp.decode():
            # New command discovered
            print("-- Success --")
            print("Hidden Command : " + sendCommand)
            # Flush the response
            Serial_Flush()
        else:
        	temp = serialPort.readline() # Needed to flush the response

# Define Main
def main():
    # Start Fuzzing
    Serial_Flush()
    print("----- Begin Fuzzing -----")

    # Fuzz lowercases
    #print("--- Fuzz lowercase letters:")
    #Fuzz_Range('a', 'z')
    
    # Fuzz Uppercases
    #print("--- Fuzz upercase letters:")
    #Fuzz_Range('A', 'Z')

    # Fuzz Numbers
    print("--- Fuzz numbers:")
    Fuzz_Range("0", "100")

# Run Main
if __name__ == '__main__':
    main()
