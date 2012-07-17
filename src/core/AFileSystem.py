'''
Created on Jul 13, 2012

@author: john
'''
import abc

class AFileSystem(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def Exists(self, path):
        """Returns if the path specified exists in the filesystem or not."""
        return
    
    @abc.abstractmethod
    def IsDir(self, path):
        """Returns if the path specified is a directoryor not."""
        return
    
    @abc.abstractmethod
    def GetSubFolders(self, path):
        """Returns the subfolders in the current folder."""
        return
    
    @abc.abstractmethod
    def Complete(self, initialPath):
        """Returns a list of paths that match the one given."""
        return