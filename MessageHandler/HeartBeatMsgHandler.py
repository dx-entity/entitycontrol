import json

from BaseMsgHandler import BaseMsgHandler
from MessageAdapter.MessageSender import MessageSender
from Utils.BaseData import BD

__author__ = 'root'

class HeartBeatMsgHandler(BaseMsgHandler):
    def __index__(self, msg):
        BaseMsgHandler.__init__(self, msg)
        self.heartResponse = dict(id=msg['id'], name=msg['name'], type='real', ipaddr=msg['ipaddr'])

    def returnHeartBeat(self):
        """
        send response
        :return:
        """
        bd = BD()
        ms = MessageSender(bd.conf)
        msg = json.dumps(self.heartResponse)
        print msg
        # ms.sendMessage()

