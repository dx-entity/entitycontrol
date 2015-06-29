from TrueEntity import TrueEntity, EntitySwitch, EntityHost, EntityRouter, EntityServer,MultiSwitch


class EntityFactory():

    @staticmethod
    def getEntity(self,data):
        entityType = {
                'switch':EntitySwitch,
                'hos':EntityHost,
                'router':EntityRouter,
                'server':EntityServer,
                'multiswitch':MultiSwitch
            }        
        etype = data.e_type
        return entityType.get(etype)(data)
        
        