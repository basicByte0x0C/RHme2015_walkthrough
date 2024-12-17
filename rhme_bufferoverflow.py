#!/usr/bin/env python

from rhme_utilities import *

#---------------------------------------
#   Implementation
#---------------------------------------

# Info and Style
print("")
print("-------------------- RHme 2015 Overflower --------------------")
print("")

# Add additional argument
parser.add_argument('-limit', type=int, help="Specify the number of characters used for input. Default: 500")
args = parser.parse_args()

# Set Overflow limit
if args.limit:
    limitValue = args.limit
else:
    limitValue = 1000

def PreCommand(command):
	# Send Command to get Device in desired state
	command += crlf
	serialPort.write(command.encode())
	temp = serialPort.readline() # Needed to flush the answer
	temp = serialPort.readline() # Needed to flush the answer

# Define Main
def main():
    # Prepare Serial
    Serial_Flush()

    # Send Command to get Device in desired state
    #PreCommand("V")

    # Write a lot of characters
    input = "A"
    for iterator in range(0, limitValue):
        input += "A"
    input += crlf
    
    # Send the Attack
    serialPort.write(input.encode())
    temp = serialPort.readline()
    print(temp.decode())

    # Show what happens
    Serial_Flush()

    # Be proud
    print("I work!")

# Run Main
if __name__ == '__main__':
    main()
