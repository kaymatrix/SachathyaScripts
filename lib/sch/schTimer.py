#For Sachathya
from PyQt5 import QtCore, QtGui, Qsci, QtWidgets
from schLib import schLookups as lookups

class schTimerCls():
		
	def __init__(self,parent):
		self.sch=parent
		self.ttls=self.sch.ttls		
		self.cmttls=self.sch.schGUIObj.cmttls
		self.sch.display("pyOneTimerCls is ready!")
		self.fnTimerDone = {}

	def initialize(self):
		self.sch.qtime=QtCore.QTimer(self.sch.schQtApp)
		self.sch.qtime.timeout.connect(self.timeoutAction)   		
		self.sch.display("pyOneTimerCls Initialized")

	def addTimerExecFunctions(self, fn, argList = ()):
		self.fnTimerDone[fn.__name__]=(fn,argList)

	def startTimer(self,secs=5):
		self.sch.display("-Timer Started-")
		self.sch.qtime.start(1000 * secs)

	def stopTimer(self):
		self.sch.display("-Timer Stopped-")
		self.sch.qtime.stop()

	def timeoutAction(self):
		self.sch.display("---Timer Timed out--")
		for eachFn in self.fnTimerDone:
			fns = self.fnTimerDone[eachFn]
			fnObj = fns[0]
			args = fns[1]
			fnObj(args)

if __name__ == '__main__':
	sch.schTimerClsObj = schTimerCls(sch)
	sch.schTimerClsObj.initialize()