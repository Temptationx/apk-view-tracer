#! python2.7
## -*- coding: utf-8 -*-

## kun for Apk View Tracing
## CommandConsole.py

import os

class CommandConsole():
    '''
    Command Console: it use adb command
    '''
    __ClassName = "CommandConsole"
    
    def __init__(self):
        self.emulator_port = 5554
        
    def executeCommand(self, cmd):
        try:
            os.system(cmd)
            return True
        except Exception, e:
            print "[%s] Failed execute cmd [%s]: [%s]" %(self.class_name, cmd, str(e))
            return False
        
    def installPkg(self, device_name, package_name):
        installPkgCmd = "adb -s %s install %s" %(device_name, package_name)
        return self.executeCommand(installPkgCmd)
    
    def removePkg(self, device_name, package_name):
        removePkgCmd = "adb -s %s uninstall %s" %(device_name, package_name)
        return self.executeCommand(removePkgCmd)
    
    ## for example:
    ## To start the Settings application: # am start -n com.android.settings/.Settings
    ##                                    # am start -n com.android.settings/com.android.settings.Settings
    ## To start the Browser: # am start -n com.android.browser/.BrowserActivity
    ##                       # am start -n com.android.browser/com.android.browser.BrowserActivity
    ## To start the Calculator # am start -n com.android.calculator2/.Calculator
    ##                         # am start -n com.android.calculator2/com.android.calculator2.Calculator
    def startActivity(self, package_name, activity_name):
        # -W must be before -n
        # -W is "start" command option, and -n is <INTENT> option
        startActivityCmd = "adb shell am start -W -n %s/.%s" %(package_name, activity_name)
        return self.executeCommand(startActivityCmd)
    
    ## To start the phone dialer: # am start tel:210-385-0098
    def startPhoneDialer(self, phone_number):
        startPhoneDialerCmd = "adb shell am start tel:%s" %str(phone_number)
        return self.executeCommand(startPhoneDialerCmd)
    
    def startService(self, service_name):
        startServiceCmd = "adb shell am startservice %s" %service_name
        return self.executeCommand(startServiceCmd)
        
    def sendBroadcastIntent(self, broadcast_name):
        sendIntentCmd = "adb shell am broadcast %s" %broadcast_name
        return self.executeCommand(sendIntentCmd)
    
    def startInstrumentation(self, component_name):
        startInstrumentationCmd = "adb shell am instrument -w %s" %component_name
        return self.executeCommand(startInstrumentationCmd)
    
    def pushFile(self, local_path, emulator_path, emulator_port=5554):
        pushFileCmd = "adb -s emulator-%s push %s %s" %(emulator_port, local_path, emulator_path)
        return self.executeCommand(pushFileCmd)
    
    def pullFile(self, emulator_path, local_path, emulator_port=5554):
        pullFileCmd = "adb -s emulator-%s pull %s %s" %(emulator_port, emulator_path, local_path)
        return self.executeCommand(pullFileCmd)
        
    def phoneCall(self):
        pass
    
    def sendSMS(self):
        pass
    
    def browseWebPage(self):
        pass
    
    