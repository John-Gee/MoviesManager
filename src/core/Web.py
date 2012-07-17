'''
Created on Jul 12, 2012

@author: john
'''
from Definitions import ServerDefinition
from mako.lookup import TemplateLookup

from MoviesListing import MoviesListing
from FileSystem import FileSystem

import json


lookup = TemplateLookup(directories=['../web'])

class Web:
    def __init__(self, httpServer, fileSystem):
        self.httpServer = httpServer
        self.fileSystem = fileSystem
        self.moviesListing = MoviesListing(self.fileSystem)
        
    def index(self):
        folder = self.httpServer.GetSessionValue("folder")
        pattern = self.httpServer.GetSessionValue("pattern")
        folders = self.httpServer.GetSessionValue("folders")
        exception = ""
            
        if folder == None:
            folder = ""
            
        if pattern == None:
            pattern = ""
            
        if folders == None:
            folders = []
        
        return lookup.get_template(ServerDefinition.templateFile).render(folder=folder, pattern=pattern, folders=folders, exception=exception)
        
    index.exposed = True
    
    def JSONInputFolder(self, folder, pattern):
        self.httpServer.SetSessionValue("folder", folder)
        self.httpServer.SetSessionValue("pattern", pattern)
        
        exception = ""
        
        folders = None
        try:
            folders = self.moviesListing.FindMatchingFoldersInPath(folder, pattern)
        except Exception as e:
            exception = "An exception was raised: {0}".format(e)
        
        jsonResponse = json.dumps([folders, exception])
        return jsonResponse        
    
    JSONInputFolder.exposed = True
    
    def GetMatchingPaths(self, initialPath):
        paths = self.fileSystem.Complete(initialPath)
        paths.sort()
        print paths
        return paths
    
    def GetJSONMatchingPaths(self, initialPath):
        paths = self.GetMatchingPaths(initialPath)
        jsonPaths = json.dumps(paths)
        print jsonPaths
        return jsonPaths
    GetJSONMatchingPaths.exposed = True
    
    