iPhoneDebugTool
===============

――――――――――――――――――――――――――――――――――――

Symbolize Memory Addresses from iPad crash file:

How to symbolize memory addresses from iPad native crash log file.

What you need:

1) the dSYM file 
2) symbolizeCrash.command script file
3) crash file

How to run symbolizeCrash.command script in terminal:

source symbolizeCrash.command <crash log file> <dSYM file> > output.txt

――――――――――――――――――――――――――――――――――――

Symbolize One Line

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

日本語版
――――――――――――――――――――――――――――――――――――

iPadからシンボライズする方法

iPadの標準クラッシュファイルからシンボライズ方法：

必要なファイル：

1) .dSYMのファイル、アーカイブから取れます。
2) 「symbolizeCrash.command」というシェルスクリプトファイル
3) シンボライズしたいのiPadの標準クラッシュファイル

「symbolizeCrash.command」実行する方法：

注意１：＊全部の必要なファイルは同じフォルダに置いてください＊
注意２：＊使用フォルダのオススメは＄HOMEです＊

ターミナルで「source symbolizeCrash.command <crash log file> <dSYM file> > <output.txt>」これを書いてください。

――――――――――――――――――――――――――――――――――――

(一つの行だけをシンボライズ）クラッシュファイルからシンボライズ方法：

必要なファイル：

1) .dSYMの中にDWARFというフォルダがあります。それの中からのファイルが必要です。
例えば: appname.app.dSYM/Contents/Resources/DWARF <―― このフォルダのなか「appname」というファイルがあります。それをmemoryAddr.pyと同じ所にコピペしてください。

2) 「memoryAddr.py」というpythonスクリプトファイル

3) サーバーからのクラッシュファイル

「memoryAddr.py」実行する方法：

ターミナルで「python memoryAddr.py」これを書いてください。

実行した後に「VMADDR」を入力してください。VMADDRは上の出力した番号から来ます。

例えば：vmaddr 0x00004000 そして、INPUT YOUR VMADDR: 0x00004000

次、シンボライズしたいのメモリアドレスを「INPUT THE MEMORY ADDRESS TO SYMBOLIZE: 」に入力してください。

例えば：INPUT THE MEMORY ADDRESS TO SYMBOLIZE:  0x002931fc

最後、プログラムのスタートアドレスが必要です。それがあれば「PLEASE INPUT THE BASE ADDRESS: 」に入力してください。

「vmaddrとメモリアドレスとbase address」この３つの16進法番号があれば、入力したメモリアドレスをシンボライズできます。
