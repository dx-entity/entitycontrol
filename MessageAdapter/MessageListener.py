from stompy.simple import Client
from MessageHandler import MessageHandlerFactory as msgf


class MessageListener(object):
    '''
    message listener 
    '''
    def __init__(self, conf):
        self.mq_server = conf.getConfig('mq_server')
        self.ec2mcu = conf.getConfig('ec2mcu')
        self.mcu2ec = conf.getConfig('mcu2ec')
        self.mcu2ec_allive = conf.getConfig('mcu2ec_allive')
        self.ec2mcu_allive = conf.getConfig('ec2mcu_allive')

    def listenMessage(self):
        client = Client('mqserver', 61613)
        client.connect()     
        client.subscribe(self.mcu2ec)
        while True:
            client.get(block=True, callback=msgf.MessageHandlerFactory.getMsgHandler)

    def listenAliveMsg(self):
        c_allive = Client('mqserver', 61613)
        c_allive.connect()
        c_allive.subscribe(self.mcu2ec_allive)
        while True:
            c_allive.get(block=True, callback=msgf.MessageHandlerFactory.getMsgHandler)