# -*- coding:UTF-8 -*- #
import MySQLdb
import MySQLdb.cursors  
import paramiko
import commands, os
from Utils.BaseData import BD


class SnmpAdapter():
    def __init__(self, ip, community):
        self._ip = ip
        self._community = community


    def __del__(self):
        pass


    def snmp_get(self, oid):
        get_command = ''.join(['snmpget -c ',self._community,' -v 2c ',self._ip,' '])+oid
        #print get_command
        return commands.getoutput(get_command)


    def snmp_walk(self, oid):
        walk_command = ''.join(['snmpwalk -c ',self._community,' -v 2c ',self._ip,' '])+oid
        #print walk_command
        return commands.getoutput(walk_command)




class DataBase:
    host, user, password, database, port ,charset= '', '', '', '', '', ''

    def __init__(self, port = 3306, charset="utf8"):
        bd = BD()
        self.host, self.user, self.password, self.database, self.port, self.charset= bd.conf.getConfig('dbserver'),bd.conf.getConfig('dbuser'),bd.conf.getConfig('dbpasswd'),bd.conf.getConfig('db'), port, charset

    def getconn(self):

        conn = MySQLdb.connect(host = self.host, user = self.user, passwd = self.password, db = self.database, port= self.port, charset=self.charset)
        mydb = conn.cursor()
        return mydb

    def doquery_tuple(self, sql_str):

        conn = MySQLdb.connect(host = self.host, user = self.user, passwd = self.password, db = self.database, port= self.port, charset=self.charset)
        cur = conn.cursor()
        cur.execute(sql_str)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def doquery(self, sql_str):

        conn = MySQLdb.connect(host = self.host, user = self.user, passwd = self.password, db = self.database, port= self.port, charset=self.charset)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        cur.execute(sql_str)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def execsql(self,sql):

        conn = MySQLdb.connect(host = self.host, user = self.user, passwd = self.password, db = self.database, port= self.port, charset=self.charset)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        return True

    def checkout(self,sql):
        '''
        check if the infomation already in database
        exist return False
        not exist return True
        '''
        result = self.doquery(sql)
        if len(result):
            return False
        else:
            return True


class VlanDealer():
    def __init__(self,ip,name,passwd):
        self.connection = paramiko.SSHClient()
        self.ip = ip
        self.name = name
        self.passwd = passwd


    def __del__(self):
        self.connection.close()


    def getConnection(self):
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection.connect(self.ip,username=self.name,password=self.passwd)
        interactive_shell = self.connection.invoke_shell()
        return interactive_shell


    def vlanCreator(self, portList,vlanId):
        if not isinstance(portList,list):
            print 'raise exception'

        interactive_shell = self.getConnection()
        interactive_shell.send('system-view\n')
        interactive_shell.send(''.join(['vlan ',vlanId,'\n']))
        for port in portList:
            interactive_shell.send(''.join(['port GigabitEthernet1/0/',port,'\n']))
        interactive_shell.send('quit\n')
        #how does interactive_shell return false
        return True
