#! /bin/bash -x 

export DEVELOPER_DIR='/Applications/Xcode.app/Contents/Developer'
alias symbolicate='./../../../../Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/PrivateFrameworks/DTDeviceKitBase.framework/Versions/A/Resources/symbolicatecrash'

#cp *.app.dSYM 
#cp *.crash

symbolicate "$1" "$2" 

#symbolicate "crashLog.crash" "aaron.app.dSYM"

function symbolicate(){
	
./../../../../Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/PrivateFrameworks/DTDeviceKitBase.framework/Versions/A/Resources/symbolicatecrash "$@" "$@"

}
