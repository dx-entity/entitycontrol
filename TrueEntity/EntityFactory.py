__author__ = 'root'

from EntityHost import *
from EntityRouter import *
from EntityServer import *
from EntitySwitch import *

class EntityFactory(object):
    """
    entity factory
    produce EntityHost, EntityRouter, EntityServer
    """

    productlist = {
        'host': EntityHost,
        'server': EntityServer,
        'router': EntityRouter,
        'switch': EntitySwitch
    }

    @staticmethod
    def getEntity(dev):
        assert dev.has_key('type') and dev['type']
        return EntityFactory.productlist[dev['type']](dev)

