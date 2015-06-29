from stompy.simple import Client
from MessageHandler import MessageHandlerFactory as msgf


class MessageListener():   
    '''
    message listener 
    '''    
    def __init__(self,conf):
        self.mq_server = conf.getConfig('mq_server')
        self.ec2mcu = conf.getConfig('ec2mcu')
        self.mcu2ec = conf.getConfig('mcu2ec')
        print self.mcu2ec
    
    def listenMessage(self):
        client = Client('mq_server',61613)
        client.connect()     
        client.subscribe(self.mcu2ec)
        while True:
            msg = client.get(block=True,callback=msgf.MessageHandlerFactory.getMsgHandler)
    

