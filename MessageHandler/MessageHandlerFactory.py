from MessageHandler.DeployMsgHandler import DeployMsgHandler
from MessageHandler.HeartBeatMsgHandler import HeartBeatMsgHandler
from MessageHandler.CloseMsgHandler import CloseMsgHandler
from MessageHandler.StartMsgHandler import StartMsgHandler
import json
import time

class MessageHandlerFactory(object):
    
    @staticmethod
    def getMsgHandler(msg):
        handler = {
            'DEPLOY': DeployMsgHandler,
            'START': StartMsgHandler,
            'CLOSE': CloseMsgHandler,
            'heartbeat': HeartBeatMsgHandler
        }
        # time.sleep(10)
        print msg.body
        dealed_msg = json.loads(msg.body)
        tastHandler = handler[dealed_msg['name']]
        # print dir(tastHandler(dealed_msg))
        tastHandler(dealed_msg).returnHeartBeat()