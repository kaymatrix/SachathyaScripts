#For Sachathya

from PyQt5 import QtCore, QtGui, Qsci, QtWidgets
from PyQt5.uic import loadUi
from schLib import schLookups as lookups
import os
import sip
import kmxQtCommonTools
import myserach

class myserachCls(QtWidgets.QMainWindow):
    
    def __init__(self,parent):
        self.tag=self.__class__.__name__.replace('Cls','').upper()
        
        self.sch=parent
        self.schGUIObj=self.sch.schGUIObj
        self.schQtApp=self.sch.schQtApp
        self.ttls=self.sch.ttls
        self.cmttls=kmxQtCommonTools.CommonTools()

        QtWidgets.QMainWindow.__init__(self)        
        self.uiFile=myserach.__file__.replace(".py",".ui")

        loadUi(self.uiFile, self)
        self.setWindowTitle(self.__class__.__name__.replace('Cls',''))

        self.pushButton.clicked.connect(self.doRun)
        
    def initialize(self):
        self.sch.display("myserachClsObj is working fine",self.tag)

    def doRun(self):
        import requests
        url = 'http://127.0.0.1:8082/getxml'
        self.xmlData = requests.get(url, verify=True).text
        self.textEdit.setText(self.xmlData)
    
    def quickSearch(self):
        from xmljson import badgerfish as bf

        val = self.lineEdit.text()
        print(val)
        
        from lxml import etree
        
        dom = etree.XML(self.xmlData)
        print(dom.tag)
        
        d = bf.data(dom)
        print(d['catalog']['book'][0][val]['$'])
        
        
        
        
        
        
        
        

if (__name__=="__main__"):
    if(not hasattr(sch, 'myserachObj') or sch.devMode or sip.isdeleted(sch.myserachObj)):
        sch.myserachObj = myserachCls(sch)
    sch.myserachObj.show()
    sch.myserachObj.raise_()