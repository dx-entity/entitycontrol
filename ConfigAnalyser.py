import ConfigParser


class ConfigAnalyser:
    def __init__(self,configFile):
        cf = ConfigParser.ConfigParser()
        cf.read(configFile)
        # log configration
        # self.log_format = cf.get('LOG','log_format')
        self.log_file = cf.get('LOG', 'log_filepath')
        # mq configration
        self.mq_server = cf.get('ActiveMQ', 'MQserver')
        self.ec2mcu = cf.get('ActiveMQ', 'EC2MCU_topic')
        self.mcu2ec = cf.get('ActiveMQ', 'MCU2EC_topic')
        self.mcu2backend_alive = cf.get('ActiveMQ', 'MCU2BACKEND_ALIVE')
        self.backend2mcu_alive = cf.get('ActiveMQ', 'BACKEND2MCU_ALIVE')

        # multi switch configuration
        self.switchlist = cf.items("Multiswitch")
        # database configuration
        self.dbserver = cf.get('DB', 'ip')
        self.user = cf.get('DB', 'user')
        self.passwd = cf.get('DB', 'passwd')
        self.db = cf.get('DB', 'db')
        # nfs configuration
        self.nfsBaseDir = cf.get('NFS', 'basedir')

    def getConfig(self, name):
        dicConfig = {
            'switchlist': self.switchlist,
            'dbserver': self.dbserver,
            'dbuser': self.user,
            'dbpasswd': self.passwd,
            'db': self.db,
            'ec2mcu': self.ec2mcu,
            'mcu2ec': self.mcu2ec,
            'mcu2ec_allive': self.mcu2backend_alive,
            'ec2mcu_allive': self.backend2mcu_alive,
            'mq_server': self.mq_server,
            'basedir': self.nfsBaseDir
        }
        return dicConfig[name]
