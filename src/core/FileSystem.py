'''
Created on Jul 13, 2012

@author: john
'''

import os.path
import glob

from AFileSystem import AFileSystem

class FileSystem(AFileSystem):
    def Exists(self, path):
        return os.path.exists(path)
    
    def IsDir(self, path):
        return os.path.isdir(path)
    
    def GetSubFolders(self, path):
        entries = os.listdir(path)
        folders = []
        for entry in entries:
            if self.IsDir(os.path.join(path, entry)):
                folders.append(entry)
        return folders
    
    def Complete(self, initialPath):
        return glob.glob(initialPath+'*')