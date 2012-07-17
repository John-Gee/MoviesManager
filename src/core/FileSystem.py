'''
Created on Jul 13, 2012

@author: john
'''

import os.path

from AFileSystem import AFileSystem

class FileSystem(AFileSystem):
    def Exists(self, path):
        return os.path.exists(path)
    
    def IsDir(self, path):
        return os.path.isdir(path)
    
    def GetFolders(self, path):
        return os.listdir(path)