import json

from BaseMsgHandler import BaseMsgHandler
from MessageAdapter.MessageSender import MessageSender
from Utils.BaseData import BD

__author__ = 'root'

class HeartBeatMsgHandler(BaseMsgHandler):
    def __init__(self, msg):
        BaseMsgHandler.__init__(self, msg)
        # print self.__class__, msg
        self.heartResponse = dict(id=msg['id'], name=msg['name'], type='real', ipaddr=msg['ipaddr'])

    def doAction(self):
        self.returnHeartBeat()

    def returnHeartBeat(self):
        """
        send response
        :return:
        """
        bd = BD()
        ms = MessageSender(bd.conf)
        msg = json.dumps(self.heartResponse)
        # print self.__class__, self.heartResponse
        print self.__class__, msg
        res = ms.sendMessage(msg)

        try:
            assert res.as_string()
        except AssertionError, args:
            print "%s: %s" % (args.__class__.__name__, args)