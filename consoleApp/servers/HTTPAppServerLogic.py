#For Sachathya
from http.server import BaseHTTPRequestHandler, HTTPServer

class httpRequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.uri = self.path.split('/')
		try:
			self.doProcess(self.uri)
		except:
			return 
		return

	def setSuccessResponse(self, response):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(bytes(response, "utf8"))
		
	def doProcess(self, uri):
		print(str(self.uri))
		response=''
		if (len(uri)>1):
			fn = uri[1]
			print(fn)
			if (fn=='getxml'):
				response = self.getXML()
			if (fn=='add'):
				param1=int(uri[2])
				param2=int(uri[3])
				response = str(param1+param2)
			if (fn=='sub'):
				param1=int(uri[2])
				param2=int(uri[3])
				response = str(param1-param2)
			if (fn=='mul'):
				param1=int(uri[2])
				param2=int(uri[3])				
				response = str(param1*param2)				
			print(response)
		self.setSuccessResponse(response)
	
	def getXML(self):
		f = open('D:\\sample.xml','r')
		data = f.read()
		f.close()
		return str(data)
