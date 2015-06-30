import os
import copy
from optparse import OptionParser

import ConfigAnalyser as ca
from MessageAdapter.MessageListener import *
from Utils.BaseData import BD
from TrueEntity.Entity import *
from GlobalData import *

def main():

    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage = usage, version="%prog 1.0")
    parser.add_option("-f", "--file", dest="configFilePath",  action="store",
                      help="config file name")
    parser.add_option("-d","--deamon",dest="runBackEnd", action="store_true", default=False,
                      help="run program as deamon")

    (options, args) = parser.parse_args()

    if len(args) == 0:
        print "using default config file config.ini"
        options.configFilePath = 'config.ini'
    if options.runBackEnd:
        print "program run in backend, pid is %s" % (os.getpid())

    #0.initial config file
    gd = GlobalDevice()
    gc = GlobalCase()
    bd = BD()

    bd.conf = ca.ConfigAnalyser(options.configFilePath)
    switchlist = bd.conf.getConfig('switchlist')
    #print switchlist

    # 1.initial all multiswitch
    for switch in switchlist:
        data = copy.deepcopy(bd.data)
        data['e_name'] = switch[0]
        data['face'] = switch[1].split(',')[0]
        data['e_ip'] = switch[1].split(',')[1]
        data['multi_switch'] = True
        data['e_type'] = 'switch'

        ms = MultiSwitch(data)
        if ms.testConnection():
            ms.dealer.selfInit()
        else:
            print data['e_name'], "connection test failed"
    # 2.check the link between switch and server


    # 3.prepare to receive msg
    ml = MessageListener(bd.conf)
    ml.listenMessage()
    ml.listenAliveMsg()

    # 4.do some cleaning if need


main()
