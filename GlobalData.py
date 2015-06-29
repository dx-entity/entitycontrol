import uuid,logging
import ConfigAnalyser

class Single(type):
    def __init__(cls, name, bases, dict):
        super(Single, cls).__init__(name, bases, dict)
        cls._instance = None  
        
    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Single, cls).__call__(*args, **kw)
            # print cls.__name__, cls._instance

        return cls._instance          
    pass


class GlobalDevice(object):
    '''
    all the device is maintained in this class object
    '''
    
    __metaclass__ = Single   #  singleton
    
    def __init__(self):
        self.name_device = {}         #store device , key: uuid, value: instence of dev
        self.caseID_device = {}       #store device, key: caseid,value: list of dev belong to this case
        pass
    
    
    def getDevByCaseID(self,caseID):
        '''
        get device by caseID,
        input caseID
        return list of device
        '''
        pass
    
    
    def getDevByName(self,name):
        '''
        get device by dev name,
        input name,
        return list of device
        '''
        if self.name_device.has_key(name):
            return self.name_device[name]
        else:
            return None
    
    
    
    def deleteDevByCaseID(self,caseID):
        '''
        delete all device belong to caseID
        input caseid
        return True if delete success else False
        '''        
        pass
    
    
    def deleteDevByName(self,name):
        '''
        delete device by name
        input name
        return True if delete success else False
        '''
        pass
    
    
    def saveDevByCaseID(self,dev_list,caseid):
        '''
        save all the device belong to caseid
        input caseid, listof device
        return True if delete success else False 
        '''        
        pass
    
    
    def saveDevByName(self,name,dev):
        '''
        save dev by name
        input name
        return True if delete success else False
        '''

        if self.name_device.has_key(name):
            print 'raise exception : duplicate name device'
            return False
        else:
            self.name_device[name] = dev
            return True



class GlobalCase(object):   
    '''
    save case data
    '''
    
    
    __metaclass__ = Single      #  singleton
    
    
    def __init__(self):
        self.case_data = {}  #save case data key:caseid value: status
        
        pass
    
    
    def getCase(self, caseid):
        '''
        get casedata according to caseid
        '''
        pass
    
    
    def saveCase(self, caseid):
        '''
        save casedata according to caseid
        '''
        pass
    
    
    def delCase(self, caseid):
        '''
        remove casedata according to caseid
        '''
        pass
