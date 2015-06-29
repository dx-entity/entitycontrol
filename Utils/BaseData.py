from EntityControl.GlobalData import Single


class BD():
    
    __metadata__=Single
    
    def __init__(self,):
        self.data = {'entity_id':'',
        'e_type':'',
        'e_name':'',
        'e_sn':'',
        'e_ip':'',
        'e_uname':'admin',
        'e_passwd':'iiecas',
        'e_isSnmp':False,
        'community_w':'iiecas_testwrite',
        'community_r':'iiecas_testread',
        'caseid':'',
        'service':[],
        'multi_switch':False}

        self.conf = None  #configAnalyser instance

        self.baseDataSnmp = {
        'snmpVersion2':'2c',
        'comunityWrite':'iiecas_testwrite',
        'h3cSwitchMIB':{
            'sn':'iso.3.6.1.2.1.47.1.1.1.1.11.2',
            'mactable':'iso.3.6.1.4.1.25506.8.35.3.1.1.1',
            'table2port':'iso.3.6.1.4.1.25506.8.35.3.2.1.2',
            'portmacaddr':'iso.3.6.1.2.1.2.2.1.6',
            'portname':'iso.3.6.1.2.1.2.2.1.2',
            'portstatus':'iso.3.6.1.2.1.2.2.1.8'
        }
        }



