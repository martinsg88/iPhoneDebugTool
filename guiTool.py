import os, os.path, subprocess, sys

class hideUnhide:

	def show(self):
		print "SHOW THE INFORMATION"

	def unHide(self):
		print ""

class symbolicate:
	
	def symbolicateStart(self):

	    var = sys.argv

	    slideStart = 'otool -arch armv7 -l "lovenama" | grep -B 3 -A 8 -m 2 "__TEXT"'
	    symbolize = "xcrun atos -arch armv7 -o lovenama"

	    print(slideStart)
	    os.system(slideStart)

	    slide = raw_input("INPUT YOUR VMADDR: ")

	    print("VMADDR = %s" % slide)

	    inputMemoryAddress = raw_input("INPUT THE MEMORY ADDRESS TO SYMBOLIZE: ")
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

	print "_________________            WELCOME TO AUTOMATION SCRIPT SELECTION _________________\n\n"

	print "_________________            PRESS 1 FOR IOS DEBUGGING                  _________________\n"

	print "_________________            PRESS 2 FOR IMAGE COMPRESSION          _________________\n"

	switchChoice = raw_input("Enter your selection: ")
	if switchChoice == '1':
		symbol.symbolicateStart()

	elif switchChoice == '2':
		change.ffmpegCheck()

if __name__=="__main__":
    main()