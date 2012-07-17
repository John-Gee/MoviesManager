'''
Created on Jul 13, 2012

@author: john
'''
from core.AFileSystem import AFileSystem

class MockFileSystem(AFileSystem):
    def __init__(self):
        self.paths = []
        self.dirs = []
        
    def AddPath(self, path, isDir):
        self.paths.append(path)
        if isDir:
            self.dirs.append(path)
    
    def Exists(self, path):
        return path in self.paths
    
    def IsDir(self, path):
        return path in self.dirs
    
    def GetFolders(self, path):
        folders = []
        for p in self.paths:
            if path in p and self.IsDir(p):
                folders.append(p)
                 
        return folders;
            
