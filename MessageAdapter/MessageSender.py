from stompy.simple import Client

class MessageSender(object):
    """
    message Sender
    """

    def __init__(self, conf):
        self.mq_server = conf.getConfig('mq_server')
        self.ec2mcu = conf.getConfig('ec2mcu')
        self.mcu2ec = conf.getConfig('mcu2ec')
        self.mcu2ec_allive = conf.getConfig('mcu2ec_allive')
        self.ec2mcu_allive = conf.getConfig('ec2mcu_allive')
        
    def sendMessage(self, msg):
        client = Client('mqserver', 61613)
        client.connect()
        print msg
        client.put(msg, self.ec2mcu)
