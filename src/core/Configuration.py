'''
Created on Jul 13, 2012

@author: john
'''
import sys
import os
import configobj
from Definitions import ServerDefinition
from librairies import ConfigPersist

class Configuration(object):
    def __init__(self):
        #If the module is executed as a script __name__ will be '__main__' and sys.argv[0] will be the full path of the module.
        if __name__ == '__main__':
            path = os.path.split(sys.argv[0])[0]
        #Else the module was imported and it has a __file__ attribute that will be the full path of the module.
        else:
            path = os.path.split(__file__)[0]  
        self.config = configobj.ConfigObj(os.path.join(path, ServerDefinition.configFile))
        
    def Save(self):
        ConfigPersist.store(self.config)