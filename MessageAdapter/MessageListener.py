from stompy.simple import Client
from MessageHandler import MessageHandlerFactory as msgf
import threading


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

    class Listener(threading.Thread):
        def __init__(inner_self, topic):
            threading.Thread.__init__(inner_self)
            inner_self.topic = topic

        def run(inner_self):
            client = Client('mqserver', 61613)
            client.connect()
            client.subscribe(inner_self.topic)
            while True:
                client.get(block=True, callback=msgf.MessageHandlerFactory.getMsgHandler)

    def listenMessage(self):
        listenTaskMsg = self.Listener(self.mcu2ec)
        listenTaskMsg.start()

    def listenAliveMsg(self):
        listenAlliveMsg = self.Listener(self.mcu2ec_allive)
        listenAlliveMsg.start()
