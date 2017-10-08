'''

Created on Sep 2, 2017

@author: npn
'''
import sachathya
sch = sachathya.core(dummy=1)

import temp.flaskServer

obj = temp.flaskServer.flaskServerCls(sch)
obj.initialize()
