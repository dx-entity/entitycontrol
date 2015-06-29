from Utils.InitDevice import SnmpAdapter,DataBase,VlanDealer
from Utils import BaseData as bd
import re
import sys


class H3CDevice():
    def __init__(self):
        pass
    
    
    def selfInit(self):
        pass
    
    
    def selfClean(self,caseid):
        pass
    
    
    
class H3CSwitchAction(H3CDevice):
    '''
    H3CSwitchAction class
    '''
    def __init__(self,device):   #TrueEntity child class
        self.device = device
        self.sa = SnmpAdapter(self.device.ip, self.device.community_w)
        self.db = DataBase()
        


    def selfInit(self):
        '''
        init multi switch 
        '''
        snmpVersion = bd.baseDataSnmp['snmpVersion2']
        snmpComm = bd.baseDataSnmp['comunityWrite']
        snmpMib_sn = bd.baseDataSnmp['h3cSwitchMIB']['sn'] 
        snmpMib_mactable = bd.baseDataSnmp['h3cSwitchMIB']['mactable']
        snmpMib_table2port = bd.baseDataSnmp['h3cSwitchMIB']['table2port']
        snmpMib_macAddr = bd.baseDataSnmp['h3cSwitchMIB']['portmacaddr']
        snmpMib_portName = bd.baseDataSnmp['h3cSwitchMIB']['portname']
        snmpMib_portStatus = bd.baseDataSnmp['h3cSwitchMIB']['portstatus']
        
        
        #insert device sn number and get device_id
        device_sn = self.sa.snmp_get(snmpMib_sn)
        pattern = re.compile(r'".*"')
        sn_num = pattern.findall(device_sn)[0].replace('"','')
        sql_check = 'select id from z_entity_control_test_switch where switch_sn_number="%s"'%(sn_num)
        print sql_check
        result = self.db.doquery(sql_check)
        if len(result):
            self.device.entity_id = result[0]['id']
        else:
            sql_insert = 'insert into z_entity_control_test_switch (switch_sn_number, ip) values ("{0}","{1}")'.format(sn_num, self.device.ip)
            print sql_insert
            self.db.execsql(sql_insert)     #try exception
            self.device.entity_id = self.db.doquery('SELECT LAST_INSERT_ID() as id')[0]['id']
            
            
        #get port status and name
        port = {}
        port_mac = self.sa.snmp_walk(snmpMib_macAddr).split('\n')
        for i in range(len(port_mac)):
            key = port_mac[i].split(':')[-1].replace(' ','-')[1:-1]
            port_name = self.sa.snmp_get('.'.join([snmpMib_portName,str(i+1)]))
            pattern = re.compile(r'".*"')
            name = pattern.findall(port_name)[0].replace('"','')
            port_status = self.sa.snmp_get('.'.join([snmpMib_portStatus,str(i+1)])).split(':')[-1].replace(' ','')
            port[key] = [name,port_status]
            sql_check = 'select id from z_entity_control_test_port where mac_address="%s"'%(key)
            if self.db.checkout(sql_check):
                sql_insert = 'insert into z_entity_control_test_port (switch_id,port_name,mac_address,state) values (%s,"%s","%s",%s)'%(self.device.entity_id,name,key,port_status)
                self.db.execsql(sql_insert)
                
            else:
                sql_update = 'update z_entity_control_test_port set state=%s where mac_address="%s"'%(port_status,key)
                self.db.execsql(sql_update)
                
                
        #get port mac table and port vlan
        mac = self.sa.snmp_walk(snmpMib_mactable).split('\n')
        
        for i in range(len(mac)):
            mac_table = mac[i].split(":")[-1][1:-1].replace(" ","-")
            print mac_table
            other_info = mac[i].split(":")[0]
            vlan_id = other_info.replace(snmpMib_mactable,'').split("=")[0].split(".")[-1].replace(" ","")
            print vlan_id
            mac_decimal = other_info.replace(snmpMib_mactable,'').split('=')[0].replace(' ','').split('.')
            mac_decimal.pop(-1)
            mac_decimal = '.'.join(mac_decimal)
            print mac_decimal
            port = self.sa.snmp_get(''.join([snmpMib_table2port,'.',vlan_id,mac_decimal]))
            port_number = port.split(':')[1].replace(" ","")
            print port_number
            port_name = 'GigabitEthernet1/0/'+port_number
            
            sql_check = 'select id from z_entity_control_test_port where port_name="%s"'%(port_name)
            print sql_check
            res = self.db.doquery(sql_check)
            if not res:
                print "raise exception"
            
            port_id = res[0]['id']
            
            sql_update = 'update z_entity_control_test_port set vlan_id=%s where id=%s'%(vlan_id,port_id)
            print sql_update
            self.db.execsql(sql_update)
            
            sql_insert = "insert into z_test_entity_control_mactable (mac_learned,port_id,switch_id) values ('%s',%s,%s)"%(mac_table,port_id,self.device.entity_id)
            self.db.execsql(sql_insert)
            
            
        print 'device self init finish need to write log'

    def vlanDealer(self,portlist):
        '''
        update database and vlan 
        '''
        vd = VlanDealer(self.device.ip, self.device.uname, self.device.passwd)
        if vd.vlanCreator(portList, vlanId):
            print 'update the database'
            pass 
            
        
    
    def trunkDealer(self):
        pass
    
    
    def selfClean(self,caseid):
        '''
        clean vlan and other configuration according to caseid
        the casedata get from global data
        '''
        pass


class H3CActionFactory():
        
    @staticmethod
    def H3CSwitch(device):
        print device.__class__
        if device.e_type == 'switch':
            return H3CSwitchAction(device)
        
        
        
    
