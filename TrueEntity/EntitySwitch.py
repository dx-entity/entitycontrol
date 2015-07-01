__author__ = 'root'
from Utils.InitDevice import DataBase as DB

from Entity import BaseEntity


class EntitySwitch(BaseEntity):
    def __init__(self, data):
        BaseEntity.__init__(self, data)
        self.selfinit()

    def selfinit(self):
        realid = str(self.real_id)
        db = DB()
        sql_init = '''
        select * from z_entity_control_test where id=%s
        ''' % (realid)
        res = db.doquery(sql_init)
        print res
