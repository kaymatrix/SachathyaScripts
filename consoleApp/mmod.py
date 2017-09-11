'''
#For Sachathya
'''

class mmodCls():
	
	def __init__(self,parent):
		self.tag="mmod"
		self.sch=parent
		self.ttls=self.sch.ttls
		self.sch.display("mmodCls is ready!", self.tag)

	def initialize(self):
		self.sch.display("mmodCls initialized!", self.tag)

if __name__ == '__main__':
	dev.mmodClsObj = mmodCls(dev)
	dev.mmodClsObj.initialize()
