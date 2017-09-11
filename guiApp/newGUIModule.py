from PyQt5 import QtCore, QtGui, Qsci, QtWidgets
from PyQt5.uic import loadUi
import os
import sip
import newGUIModule
#For DevConsole

class newGUIModuleCls(QtWidgets.QMainWindow):
	
	def __init__(self,parent):
		self.tag="newGUIModule"
		self.sch=parent
		self.ttls=self.sch.ttls

		QtWidgets.QMainWindow.__init__(self)		
		self.uiFile=newGUIModule.__file__.replace(".py",".ui")

		loadUi(self.uiFile, self)
		self.setWindowTitle(self.__class__.__name__.replace('Cls',''))

		self.pushButton.clicked.connect(self.doRun)
		
	def initialize(self):
		self.sch.display("newGUIModuleClsObj is working fine",self.tag)

	def doRun(self):
		input = self.textEdit.toPlainText()
		self.label.setText(input)
		self.parent.pylib.say(input)

if (__name__=="__main__"):
	dev.newGUIModuleObj = newGUIModuleCls(dev)
	dev.newGUIModuleObj.show()
	dev.newGUIModuleObj.raise_()