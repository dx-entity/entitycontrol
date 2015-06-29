from stompy.simple import Client

class MessageSender():
    '''
    message Sender
    '''

    def __init__(self,conf):
        pass

    def getConn(self,conf):
        self.client = Client()
        self.conn = self.client.connect()
        
    
    def sendMessage(self, msg):
        pass
