import os
import sys

def main():

    var = sys.argv

    print 'Supported Processors arm7, arm7s, arm64'
        
    finish = False 

    while finish != True:
        processorType = raw_input("Please Tell me what processor you are using: ")
        if processorType == 'arm7' or processorType == 'arm7s' or processorType == 'arm64':
            finish = True

    applicationName = raw_input("Please input the application name: ")

    slideStart = 'otool -arch '+processorType+' -l "'+applicationName+'" | grep -B 3 -A 8 -m 2 "__TEXT"'
	    
    symbolize = 'xcrun atos -arch '+processorType+' -o '+applicationName+' '            

    print(slideStart)

    os.system(slideStart)

    slide = raw_input("INPUT YOUR VMADDR: ")
        
    finish = False

    while finish != True:
        if "64" in processorType:
            if len(slide) != 18:
                print "not a 64 bit number! please input again!"
                slide = raw_input("INPUT YOUR VMADDR: ")
            else:
                finish = True
        else:
            finish = True

    print("VMADDR = %s" % slide)

    inputMemoryAddress = raw_input("Input the memory address to symbolize:")
            
    finish = False

    while finish != True: 
        if "64" in processorType:
            if len(inputMemoryAddress) != 18:
                print "not a 64 bit number! please input again!"            
                inputMemoryAddress = raw_input("Input the memory address to symbolize:")
            else:
                finish = True
        else:
            finish = True
	    
    loadAddress = raw_input("PLEASE INPUT THE BASE ADDRESS: ")
		
    symbolize = symbolize + self.add_hex(slide, inputMemoryAddress, loadAddress)

    print(symbolize)

    os.system(symbolize)

def add_hex(hex1, hex2, hex3):
    return hex(int(hex1, 0) + int(hex2, 0) - (int(hex3, 0)))

if __name__ == "__main__":
    main()








