'''

Created on Sep 2, 2017

@author: npn
'''
from PyQt5 import QtCore, QtGui, Qsci, QtWidgets
import sys
import sachathya

sys.path.append('F:\\PythonWorkspace\\SachathyaScripts\\temp')
import temp.HTTPBasedAppServer as tf


sch = sachathya.core(dummy=1)
sch.schQtApp = QtWidgets.QApplication(sys.argv)
sch.schGUIObj = None

#----------------------------------
obj = tf.HTTPBasedAppServerCls(sch)
obj.initialize()
#----------------------------------

wins = sch.schQtApp.topLevelWidgets()
if len(wins): wins[0].closeEvent = sch.schDoInstanceLastAction                
sys.exit(sch.schQtApp.exec_())