'''
Created on Jul 13, 2012

@author: john
'''
import re

class FilesystemError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class BadPath(FilesystemError): pass
class NotADir(FilesystemError): pass

class MoviesListing(object):
        
    def FindMatchingFoldersInPath(self, path, pattern, fileSystem):
        if(not fileSystem.Exists(path)):
            raise BadPath("The path {0} specified does not exist".format(path))
        
        if(not fileSystem.IsDir(path)):
            raise NotADir("The path {0} specified is not a directory".format(path))
        
        folders = fileSystem.GetFolders(path)
        
        if pattern:
            folders = self.MatchedFolders(folders, pattern)
        
        if not folders:
            return None
        
        folders.sort()
        return folders
    
    def MatchedFolders(self, folders, pattern):
        
        if not folders:
            return None
        
        if (not pattern) or (pattern == ".*"):
            return folders
        
        rp = re.compile(pattern)
        
        foldersSubset = []
        
        for f in folders:
            match = rp.match(f)
            if match:
                foldersSubset.append(f)
                
        return foldersSubset