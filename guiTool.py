import os, os.path, subprocess, sys

class hideUnhide:

	def show(self):

		print "SHOW THE INFORMATION"

	def unHide(self):

		print ""

class symbolicate:
	
	def symbolicateStart(self):

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

	def add_hex(self, hex1, hex2, hex3):
		
		return hex(int(hex1, 0) + int(hex2, 0) - (int(hex3, 0)))

class changeRotate:

	def ffmpegCheck(self):

	    myexec = 'ffmpeg'

	    try:
	        subprocess.call([myexec, '--version'])
	        os.system('clear')
	        self.convert()

	    except OSError:
	        print "%s not found on path please install to use this software" % myexec

	def convert(self):

	    path_to_dir = raw_input("Enter the directory to convert: ")

	    crf = raw_input("Enter the CRF you wish to use: ")

	    transpose = raw_input("Enter 1 if you would like to rotate 90 degrees or 0 to do nothing: ")

	    if transpose == '1':
	    	transposeString = "transpose=1"
	    else:
	    	print "will not tranpose"

	    mov = ".mov"

	    mp4 = ".mp4"

	    files_in_dir = os.listdir(path_to_dir)

	    for file_in_dir in files_in_dir:
	        for files_in_dir in files_in_dir:	    
	            new_file = files_in_dir.replace('.mov','.mp4')	    
	            if mov in files_in_dir:	    
	                if transpose == '1':
	                    os.system('ffmpeg -i '+files_in_dir+' -crf '+crf+' -vf "'+transposeString+'" compressed_'+crf+'_'+new_file)
	                else:
	                    os.system('ffmpeg -i '+files_in_dir+' -crf '+crf+' compressed_'+crf+'_'+new_file)

def main():

	symbol = symbolicate()		

	change = changeRotate()

	print "_________________WELCOME TO AUTOMATION SCRIPT SELECTION_________________\n\n"

	print "_________________PRESS 1 FOR IOS DEBUGGING______________________________\n"

	print "_________________PRESS 2 FOR IMAGE COMPRESSION__________________________\n"

	switchChoice = raw_input("Enter your selection: ")

	if switchChoice == '1':
		symbol.symbolicateStart()

	elif switchChoice == '2':
		change.ffmpegCheck()

if __name__=="__main__":
    main()
