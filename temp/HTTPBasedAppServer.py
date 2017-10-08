#For Sachathya
from PyQt5 import QtCore, QtGui, Qsci, QtWidgets
from PyQt5.uic import loadUi
import os
import sip
import HTTPBasedAppServer
#For DevConsole
from http.server import HTTPServer, BaseHTTPRequestHandler
import HTTPAppServerLogic as coreLogicServer
HOST, PORT = '127.0.0.1', 8082

import importlib 
importlib.reload(coreLogicServer)

class HttpDaemon(QtCore.QThread):
	
	def run(self):
		self._server = HTTPServer((HOST, PORT), coreLogicServer.httpRequestHandler)
		self._server.serve_forever()

	def stop(self):
		self._server.socket.close()
		QApplication.processEvents()	
		self._server.server_close()	
		QApplication.processEvents()		
		self._server.shutdown_request(self._server.socket)
		QApplication.processEvents()		
		del(self._server)
		QApplication.processEvents()		
		#self._server.shutdown()		
		#self.wait()
		QApplication.processEvents()	

class HTTPBasedAppServerCls():
	
	def __init__(self,parent):
		self.tag=self.__class__.__name__.replace('Cls','').upper()
		self.sch=parent
		self.ttls=self.sch.ttls
		self.cmttls=kmxQtCommonTools.CommonTools()
		self.sch.display("flaskServer is readyccc!", self.tag)
		
	def initialize(self):
		self.server = HttpDaemon()
		self._print("Started HTTP Server")
		self._print("Try the url...")
		self._print("http://%s:%s/add/121/434'"%(HOST,PORT))		
		self._print("HTTPBasedAppServerClsObj is working fine")
		

		QApplication.processEvents()
		
	
		self.win, self.layout, lst = self.cmttls.createVerticalWindow(self.sch.schGUIObj, self.tag, None)

		self.win.startBtn = QtWidgets.QPushButton('Start', self.win)
		self.win.startBtn.clicked.connect(self.doStartServer)
		self.layout.addWidget(self.win.startBtn)

		self.win.stopBtn = QtWidgets.QPushButton('Stop', self.win)
		self.win.stopBtn.clicked.connect(self.doStopServer)
		self.layout.addWidget(self.win.stopBtn)
		
		#self.win.setModal(1)
		self.win.show()		
		self.sch.display("flaskServer initialized!", self.tag)	

	def doStartServer(self):
		#self.parent.setVisible(0)
		self.server.start()
		self._print('Server Started!')

	def doStopServer(self):
		self.server.stop()
		self._print('Server Stopped!')
	
	def _print(self,info=''):
		QApplication.processEvents()
		print(info)
		QApplication.processEvents()	
		
if (__name__=="__main__"):
	
	sch.obj2 = HTTPBasedAppServerCls(sch)
    print(sch.obj2)
	sch.obj2.initialize()