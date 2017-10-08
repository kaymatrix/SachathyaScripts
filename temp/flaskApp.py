#For Sachathya
from schLib import schLookups as lookups
from flask import Flask
from PyQt5.QtCore import QThread

PORT = 5000
ROOT_URL = 'http://localhost:{}'.format(PORT)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hellow world'

class FlaskThread(QThread):
    def __init__(self, application):
        QThread.__init__(self)
        self.application = application
    
    def __del__(self):
        self.wait()
    
    def run(self):
        print('Starting...')
        self.application.run(port=PORT)

class flaskAppCls():
    
    def __init__(self,parent):
        self.tag=self.__class__.__name__.replace('Cls','').upper()
        self.sch=parent
        self.ttls=self.sch.ttls
        self.sch.display("flaskApp is ready!", self.tag)

    def initialize(self):
        self.webapp = FlaskThread(app)
        self.webapp.start()        
        self.sch.display("flaskApp done!", self.tag)
        

if __name__ == '__main__':
    if(not hasattr(sch, 'flaskAppObj') or sch.devMode):	
        sch.flaskAppObj = flaskAppCls(sch)
    sch.flaskAppObj.initialize()