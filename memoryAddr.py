import os
import sys

def main():
    var = sys.argv

    slideStart = 'otool -arch armv7 -l "aaron" | grep -B 3 -A 8 -m 2 "__TEXT"'
    symbolize = "xcrun atos -arch armv7s -o aaron "

    print(slideStart)
    os.system(slideStart)

    slide = raw_input("INPUT YOUR VMADDR: ")

    print("VMADDR = %s" % slide)

    inputMemoryAddress = raw_input("INPUT THE MEMORY ADDRESS TO SYMBOLIZE: ")
    loadAddress = raw_input("PLEASE INPUT THE BASE ADDRESS: ")
	

    symbolize = symbolize + add_hex(slide, inputMemoryAddress, loadAddress)

    print(symbolize)
    os.system(symbolize)

def add_hex(hex1, hex2, hex3):
    return hex(int(hex1, 0) + int(hex2, 0) - (int(hex3, 0)))

if __name__ == "__main__":
    main()








