from BaseMsgHandler import *
from TrueEntity.EntityFactory import EntityFactory
from TrueEntity.EntityHost import *
from TrueEntity.EntityRouter import *
from TrueEntity.EntityServer import *
from GlobalData import GlobalDevice as GD

class DeployMsgHandler(BaseMsgHandler):
    def __init__(self, msg):
        BaseMsgHandler.__init__(self, msg)
        self.gd = GD()
        self.analyseXML()

    def initDevice(self, devicelist):
        # 1.test connection
        # 2.port link status
        # 3.vlan or route
        for device in self.devicelist:
            dev = EntityFactory.getEntity(device)
            self.gd.saveDevByName("name", dev)

    def initCase(self):
        self.initDevice(self.devicelist)
        assert self.msg.has_key('caseid')
        case = Case(self.msg['caseid'], "run", self.devicelist)
        self.gc.saveCase(case)

    def doAction(self):
        '''
        analyse vlan and provide link
        '''
        self.initCase()

