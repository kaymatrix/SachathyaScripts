'''
#For Sachathya
'''
from schLib import schLookups as lookups

class firstModCls():
	
	def __init__(self,parent):
		self.tag="firstMod"
		self.sch=parent
		self.ttls=self.sch.ttls
		self.sch.display("firstModCls is ready!", self.tag)

	def initialize(self):
		self.sch.display("firstModCls initialized!", self.tag)

if __name__ == '__main__':
	dev.firstModClsObj = firstModCls(dev)
	dev.firstModClsObj.initialize()