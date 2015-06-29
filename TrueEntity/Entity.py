import DeviceExtensions.H3CActionFactory as factory


class BaseEntity(object):
    '''
    base class if all entity and define some test method
    '''
    
    def __init__(self, data):
        self.entity_id = data['entity_id']
        self.e_type = data['e_type']
        self.name = data['e_name']
        self.sn = data['e_sn']
        self.ip = data['e_ip']
        self.uname = data['e_uname']
        self.passwd = data['e_passwd']
        self.isSnmp = data['e_isSnmp'] # a bool 
        self.service = data['service'] # a list of service
        self.caseid = data['caseid']
        self.community_w = data['community_w']
        self.community_r = data['community_r']
        self.multi_switch = data['multi_switch']
        
        
    def testConnection(self):
        '''
        test the decive is connectable
        return bool
        '''
        pass
    
    
    def getConnection(self):
        '''
        connect to this device
        '''
        pass
    
     
    
    
class MultiSwitch(BaseEntity):
    '''
    '''
    def __init__(self,data):
        BaseEntity.__init__(self,data)
        self.face = data['face']  #value: inner ; outter ;    
        
    
    def getDealer(self):
        self.dealer = factory.H3CActionFactory.H3CSwitch(self)
