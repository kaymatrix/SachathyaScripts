from PyQt5 import QtCore, QtGui, Qsci, QtWidgets
from PyQt5.uic import loadUi
import os
import sip
import myspl
#For DevConsole

class mysplCls(QtWidgets.QMainWindow):
	
	def __init__(self,parent):
		self.tag="myspl"
		self.sch=parent
		self.ttls=self.sch.ttls

		QtWidgets.QMainWindow.__init__(self)		
		self.uiFile=myspl.__file__.replace(".py",".ui")

		loadUi(self.uiFile, self)
		self.setWindowTitle(self.__class__.__name__.replace('Cls',''))

		self.pushButton.clicked.connect(self.doRun)
		
	def initialize(self):
		self.sch.display("mysplClsObj is working fine",self.tag)

	def doRun(self):
		input = self.textEdit.toPlainText()
		self.label.setText(input)
		self.sch.display("Sample: " + input, self.tag)

if (__name__=="__main__"):
	dev.mysplObj = mysplCls(dev)
	dev.mysplObj.show()
	dev.mysplObj.raise_()