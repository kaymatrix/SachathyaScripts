#For Sachathya
import requests
from lxml import etree
from xmljson import yahoo as xj
from collections import namedtuple
import json

def getURLData(url):
    data = requests.get(url).text
    return str(data)
    
def xmlDom(xmlStr):
    dom = etree.XML(xmlStr)
    return dom

def xml2jsonDict(xmlStr):
    dom = xmlDom(xmlStr)
    jsonDict = xj.data(dom)
    return jsonDict
    
def xml2json(xmlStr):    
    jsonDict = xml2jsonDict(xmlStr)
    jsonStr = json.dumps(jsonDict)
    return jsonStr

def xml2Obj(xmlStr):
    jsonStr = xml2json(xmlStr)    
    obj = json2Obj(jsonStr)
    return obj

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(jsonStr): return json.loads(jsonStr, object_hook=_json_object_hook)
def getMachineName(): return __builtins__['sch'].ttls.getSystemName()
def readFile(fileName): return __builtins__['sch'].ttls.fileContent(fileName)
def writeFile(fileName, data): return __builtins__['sch'].ttls.writeFileContent(fileName,data)
def doEncrypt(text, key='1234'): return __builtins__['sch'].ttls.encrypt(text,key)
def doDecrypt(text, key='1234'): return __builtins__['sch'].ttls.decrypt(text,key)
