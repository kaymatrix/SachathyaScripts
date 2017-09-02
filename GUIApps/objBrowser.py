#For DevConsole
import inspect
import os

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
import objBrowser

class objBrowserCls(QDialog):

	def __init__(self, parent=None):
		self.parent = parent
		super(objBrowserCls, self).__init__(parent)
		self.uiName=objBrowser.__file__.replace(".py",".ui")
		self.setupUI(self.uiName)
		self.parent.pylib.say("Loaded!")
		self.lineEdit.setText("self.parent")
		self.skipBuiltInsObj = False
		
		self.objInspectSpl()

	def setupUI(self, uiFile):
		prepath = os.path.abspath(os.curdir)
		prepath = os.path.join(prepath, "devPlugs")
		loadUi(uiFile, self)
		self.setWindowTitle(self.__class__.__name__)

	def skipBuiltIns(self, args):
		self.skipBuiltInsObj = args
		self.objInspectSpl()

	def inputReturn(self):
		self.objInspectSpl()

	def itemDblClicked(self, *arg):
		self.objInspectDblClick(arg)

	def itemClicked(self, *arg):
		self.objInspectClick(arg)

	def objInspectSpl(self):
		val = str(self.lineEdit.text())
		members = inspect.getmembers(eval(val))
		self.treeWidget.clear()
		for eachMember in members:
			obj = eachMember[1]
			mem = eachMember[0]
			tp = 'Obj'
			if inspect.isfunction(obj) or inspect.ismethod(obj):
				tp = 'Fn'
			elif inspect.isbuiltin(obj):
				tp = 'BuiltIn'
			elif inspect.isclass(obj):
				tp = 'Class'
			elif inspect.ismodule(obj):
				tp = 'Module'
			elif inspect.iscode(obj):
				tp = 'Code'
			elif (type(obj) is type(1) or
				type(obj) is type('') or
				type(obj) is type([]) or
				type(obj) is type(()) or
				type(obj) is type({})
			  ):
				tp = 'Variable'
			elif type(obj) is type(None):
				tp = 'Obj'
			else:
				tp = 'Obj'

			if(tp=='BuiltIn'):
				if(not self.skipBuiltInsObj):
					self.item = QtWidgets.QTreeWidgetItem()
					self.item.setText(0, mem)
					self.item.setText(1, tp)
					setattr(self.item, 'dx', eachMember[1])
					self.treeWidget.addTopLevelItem(self.item)
				
			else:
				self.item = QtWidgets.QTreeWidgetItem()
				self.item.setText(0, mem)
				self.item.setText(1, tp)
				setattr(self.item, 'dx', eachMember[1])
				self.treeWidget.addTopLevelItem(self.item)

	def objInspectClick(self, *arg):
		arg = arg[0]
		if len(arg) > 0:
			itm = arg[0]

			nam = str(itm.text(0))
			tp = str(itm.text(1))
			obj = getattr(itm, 'dx')

			try:
				doc = inspect.getdoc(obj)
				comments = inspect.getcomments(obj)
				if inspect.isfunction(obj) or inspect.ismethod(obj):
					args = str(inspect.getargspec(obj).args)
					argsDefault = str(inspect.getargspec(obj).defaults)
				else:
					args = 'Not Available'
					argsDefault = 'Not Available'
			except:
				args = ''
				argsDefault = ''
				doc = obj.__doc__
				comments = ''
			
			#ArgSpec(args=['self', 'format'], varargs=None, keywords=None, defaults=('%Y-%m-%d %H:%M:%S',))

			info = ''
			info += '\nName: %s' % (str(nam))
			info += '\nType: %s' % (str(tp))
			info += '\n\nInfo: %s' % (str(obj))
			info += '\n\nArgs: %s' % (str(args))
			info += '\nArgsDefault: %s' % (str(argsDefault))			
			info += '\n\nDoc: %s\n\n' % (str(doc))
			info += '\nComments: %s\n\n' % (str(comments))

			self.textBrowser.setText(info)

	def objInspectDblClick(self, *arg):
		arg = arg[0]
		if len(arg) > 0:
			itm = sitm = arg[0]

			nam = str(itm.text(0))
			tp = str(itm.text(1))
			obj = getattr(itm, 'dx')

			self.objInsp_In_popList(itm, obj)

	def objInsp_In_popList(self, item, data):
		prn = self

		members = inspect.getmembers(data)

		for i in range(0, item.childCount()):
			ch = item.child(i)
			item.removeChild(ch)

		for eachMember in members:
			obj = eachMember[1]
			mem = eachMember[0]
			tp = 'Obj'
			if inspect.isfunction(obj) or inspect.ismethod(obj):
				tp = 'Fn'
			elif inspect.isbuiltin(obj):
				tp = 'BuiltIn'
			elif inspect.isclass(obj):
				tp = 'Class'
			elif inspect.ismodule(obj):
				tp = 'Module'
			elif inspect.iscode(obj):
				tp = 'Code'
			elif (type(obj) is type(1) or
				type(obj) is type('') or
				type(obj) is type([]) or
				type(obj) is type(()) or
				type(obj) is type({})
			  ):
				tp = 'Variable'
			elif type(obj) is type(None):
				tp = 'Obj'
			else:
				tp = 'Obj'

			if(tp=='BuiltIn'):
				if(not self.skipBuiltInsObj):
					prn.item = QtWidgets.QTreeWidgetItem()
					prn.item.setText(0, mem)
					prn.item.setText(1, tp)
					setattr(prn.item, 'dx', eachMember[1])
					item.addChild(prn.item)				
			else:
				prn.item = QtWidgets.QTreeWidgetItem()
				prn.item.setText(0, mem)
				prn.item.setText(1, tp)
				setattr(prn.item, 'dx', eachMember[1])
				item.addChild(prn.item)

if '__main__' == __name__:
	if(not hasattr(dev,'objBrowserClsObj') or dev.devMode):	   
		dev.objBrowserClsObj = objBrowserCls(dev)
	dev.objBrowserClsObj.show()
	#dev.objBrowserClsObj._raise()
