'''
Created on Jul 12, 2012

@author: john
'''
import sys
from Definitions import ServerDefinition
from mako.lookup import TemplateLookup

from MoviesListing import MoviesListing
from FileSystem import FileSystem


lookup = TemplateLookup(directories=['../web'])

class HelloWorld:
    def __init__(self, httpServer):
        self.httpServer = httpServer
        self.moviesListing = MoviesListing()
        
    def index(self):
        folder = self.httpServer.GetSessionValue("folder")
        pattern = self.httpServer.GetSessionValue("pattern")
        folders = self.httpServer.GetSessionValue("folders")
        exception = ""
            
        if pattern == None:
            pattern = ""
            
        if folders == None:
            folders = []
        
        return lookup.get_template(ServerDefinition.templateFile).render(folder=folder, pattern=pattern, folders=folders, exception=exception)
        
    index.exposed = True
    
    def inputFolder(self, folder, pattern):
        self.httpServer.SetSessionValue("folder", folder)
        self.httpServer.SetSessionValue("pattern", pattern)
        
        exception = ""
        
        folders = None
        try:
            folders = self.moviesListing.FindMatchingFoldersInPath(folder, pattern, FileSystem())
        except Exception as e:
            exception = "An exception was raised: {0}".format(e)
        
        return lookup.get_template(ServerDefinition.templateFile).render(folder=folder, pattern=pattern, folders=folders, exception=exception)
    
    inputFolder.exposed = True
    
    def GetMatchingPath(self, InitialPath):
        return "toto"
    GetMatchingPath.exposed = True