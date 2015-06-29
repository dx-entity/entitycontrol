from MessageHandler import DeployMsgHandler, StartMsgHandler, CloseMsgHandler
import json
import time

class MessageHandlerFactory():
    
    @staticmethod
    def getMsgHandler(msg):
        handler = {
            'DEPLOY':DeployMsgHandler,
            'START':StartMsgHandler,
            'CLOSE':CloseMsgHandler
        }
        time.sleep(10)
        dealed_msg = json.loads(msg.body)
        tastHandler = handler(dealed_msg['name'])
        taskHandler(dealed_msg).doAction()
        
