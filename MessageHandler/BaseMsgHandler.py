from xml.etree import ElementTree as et
from Utils.BaseData import BD
from GlobalData import GlobalCase
import re
from MessageAdapter import MessageSender as ms


class TaskData(object):
    """
    taskData structure include taskid,caseid
    task status: finish:0, new:1, error:2
    """

    def __init__(self, caseid, taskid):
        self.caseid = caseid
        self.taskid = taskid
        self.taskstatus = 0
        self.errorMsg = "normal"

    def getTaskstatus(self):
        return self.taskstatus, self.errorMsg

    def setTaskErrorMsg(self, msg):
        self.errorMsg = msg


class Case(object):
    """
    case structure include casid, status,
    currenttasklist contains unfinished task id
    """

    def __init__(self, caseid, casestatus, devicelist):
        self.caseid = caseid
        self.casestattus = casestatus
        self.currenttasklist = {}
        self.finishtasklist = {}
        self.errortasklist = {}
        self.devicelist = devicelist

    def changestatus(self, status):
        self.casestattus = status

    def changetask(self, task):
        assert isinstance(task, TaskData)
        if task.taskstatus == 0 and self.currenttasklist.has_key(task.taskid):
            del self.currenttasklist[task.taskid]
            self.finishtasklist[task.taskid] = task
        elif task.taskstatus == 1:
            self.currenttasklist[task.taskid] = task
        elif task.taskstatus == 2:
            self.errortasklist[task.taskid] = task

    def gettask(self, taskid):
        if self.finishtasklist.has_key(taskid):
            return self.finishtasklist[taskid].getTaskstatus()
        elif self.errortasklist.has_key(taskid):
            return self.errortasklist[taskid].getTaskstatus()
        else:
            return self.errortasklist[taskid].getTaskstatus()

class BaseMsgHandler(object):
    def __init__(self, msg):
        self.devicelist = []
        self.gc = GlobalCase()
        self.bd = BD()
        self.heartResponse = None
        self.msg = msg

    def doAction(self):
        pass

    def analyseXML(self):
        """
        analyseXML get device list
        :return:devicelist
        """
        assert self.msg.has_key('tfile')
        path = self.bd.conf.getConfig('basedir') + self.msg['tfile']
        xmlDoc = et.parse(path)
        root = xmlDoc.getroot()
        topo_stucture = root.getchildren()
        pattern = re.compile(r"real_.*")
        for node in topo_stucture:
            if pattern.match(node.tag):
                dev = dict(type=node.tag.split('_')[-1],
                           real_id=node.attrib['real_id'],
                           link=[])
                chnodelist = node.getchildren()
                for ch in chnodelist:
                    if ch.tag == 'interface':
                        gchnodelist = ch.getchildren()
                        for gch in gchnodelist:
                            if gch.tag == 'link':
                                dev['link'].append(gch.text)
                self.devicelist.append(dev)
        print self.__class__, self.devicelist

    def returnWithoutHandler(self):
        pass

    def returnHeartBeat(self):
        pass
