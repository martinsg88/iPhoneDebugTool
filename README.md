iPhoneDebugTool
===============

Iphone symbolize python script

Symbolize one line from server crash log file

What you need to run the program:

1) the file inside DWARF inside dSYM

for example: appname.app.dSYM/Contents/Resources/DWARF
Inside here is a file named appname, please copy this file to the same place as memoryAddr.py

2) python script file memoryAddr.py
3) crash file from server

to run the script type;

python memoryAddr.py

This will ask you for the VMADDR which is found from the output line vmaddr.
for example

vmaddr 0x00004000

INPUT YOUR VMADDR: 0x00004000

Next, please input the memory address you want to symbolize

INPUT THE MEMORY ADDRESS TO SYMBOLIZE:  0x002931fc

Next, please input the input base address of the program

PLEASE INPUT THE BASE ADDRESS: 0x9F000
