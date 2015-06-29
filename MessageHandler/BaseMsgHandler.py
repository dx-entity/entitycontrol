from xml.etree import ElementTree as et
from EntityControl.MessageAdapter import MessageSender as ms

class BaseMsgHandler():
    def __init__(self, msg):
        pass    
    
    def doAction(self):
        pass


    def analyseXML(self):
        pass


    def returnWithoutHandler(self):
        pass


    def returnHeartBeat(self):
        pass


