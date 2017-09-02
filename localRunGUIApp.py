'''
Created on Sep 2, 2017

@author: npn
'''
from PyQt5 import QtCore, QtGui, Qsci, QtWidgets
import sys
import sachathya

from guiApp import objBrowser

dev = sachathya.core()
dev.schQtApp = QtWidgets.QApplication(sys.argv)

dev.obj = objBrowser.objBrowserCls(dev)
dev.obj.show()

wins = dev.schQtApp.topLevelWidgets()
if len(wins): wins[0].closeEvent = dev.schDoInstanceLastAction                
sys.exit(dev.schQtApp.exec_())
