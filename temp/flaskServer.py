#For Sachathya
from schLib import schLookups as lookups
from PyQt5 import QtCore, QtGui, Qsci, QtWidgets
from flask import Flask
from PyQt5.QtWidgets import QApplication
import kmxQtCommonTools
import flaskFns

PORT = 5000
ROOT_URL = 'http://localhost:{}'.format(PORT)

from flask import request


class FlaskThread(QtCore.QThread):
	
	def run(self):		
		print('Starting...' + str(ROOT_URL))
		QApplication.processEvents()
		self.fapp = flaskFns.app
		self.fapp.run(port=PORT, debug=True, use_reloader=False)
		QApplication.processEvents()
	
	def stop(self):
		QApplication.processEvents()
		self.terminate()
		self.quit()
		self.wait()
		QApplication.processEvents()
				
		
class flaskServerCls():
	
	def __init__(self,parent):
		self.tag=self.__class__.__name__.replace('Cls','').upper()
		self.sch=parent
		self.ttls=self.sch.ttls
		self.cmttls=kmxQtCommonTools.CommonTools()
		self.sch.display("flaskServer is ready!", self.tag)

	def initialize(self):
		self.flaskObj = FlaskThread()
		QApplication.processEvents()
		self.sch.display("flaskServer initialized!", self.tag)
		print('Initializing...' + str(ROOT_URL))		
		self.win, self.layout, lst = self.cmttls.createVerticalWindow(self.sch.schGUIObj, self.tag, None)

		self.win.startBtn = QtWidgets.QPushButton('Start', self.win)
		self.win.startBtn.clicked.connect(self.doStart)
		self.layout.addWidget(self.win.startBtn)

		self.win.stopBtn = QtWidgets.QPushButton('Stop', self.win)
		self.win.stopBtn.clicked.connect(self.doStop)
		self.layout.addWidget(self.win.stopBtn)
		
		#self.win.setModal(1)
		self.win.show()		
		
	def doStart(self):
		print('Start...')
		self.flaskObj.start()

	def doStop(self):
		print('Stop...')
		self.flaskObj.stop()

if __name__ == '__main__':
	if(not hasattr(sch, 'flaskServerObj') or sch.devMode):	
		sch.flaskServerObj = flaskServerCls(sch)
	sch.flaskServerObj.initialize()
