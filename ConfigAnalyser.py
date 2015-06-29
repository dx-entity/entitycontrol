import ConfigParser


class ConfigAnalyser:
    def __init__(self,configFile):
        cf = ConfigParser.ConfigParser()
        cf.read(configFile)
        #log configration
        #self.log_format = cf.get('LOG','log_format')
        self.log_file = cf.get('LOG','log_filepath')
        #mq configration
        self.mq_server = cf.get('ActiveMQ','MQserver')
        self.ec2mcu = cf.get('ActiveMQ','EC2MCU_topic')
        self.mcu2ec = cf.get('ActiveMQ','MCU2EC_topic')
        #multi switch configuration
        self.switchlist = cf.items("Multiswitch")
        #database configuration
        self.dbserver = cf.get('DB','ip')
        self.user = cf.get('DB','user')
        self.passwd = cf.get('DB','passwd')
        self.db = cf.get('DB','passwd')
        
        
    def getConfig(self,name):
        dicConfig = {
            'switchlist':self.switchlist,
            'dbserver':self.dbserver,
            'dbuser':self.user,
            'dbpasswd':self.passwd,
            'db':self.db,
            'ec2mcu':self.ec2mcu,
            'mcu2ec':self.mcu2ec,
            'mq_server':self.mq_server
        }
        return dicConfig[name]

    