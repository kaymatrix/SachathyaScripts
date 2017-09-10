import sys
import inspect

#for each in sys.path:
#    print(each)
    	
def runMe(name):
    print('Helo '+name)
    
print('This is from Sachathya Script, Thanks for running me')

import os

caller = sys._getframe(7) 

print(caller)

print ("Called from module", caller.f_globals['__name__'])
print(os.path.abspath(os.curdir))
print(dev.schArgParserObj.schScriptFolder)	
print(__name__)