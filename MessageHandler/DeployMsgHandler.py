from BaseMsgHandler import *
from TrueEntity.EntityHost import *
from TrueEntity.EntityRouter import *
from TrueEntity.EntityServer import *

class DeployMsgHandler(BaseMsgHandler):
    def __init__(self, msg):
        BaseMsgHandler.__init__(self, msg)

    def initDevice(self, devicelist):
        # 1.test connection
        # 2.port link status
        # 3.vlan or route
        for device in devicelist:
            pass
        pass

    def initCase(self):
        devicelist = self.analyseXML()
        self.initDevice(devicelist)
        assert self.msg.has_key('caseid')
        case = Case(self.msg['caseid'], "run", devicelist)
        self.gc.saveCase(case)

    def doAction(self):
        '''
        analyse vlan and provide link
        '''
        
        pass
