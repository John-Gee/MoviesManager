'''
Created on Jul 12, 2012

@author: john
'''

from HTTPServer import HTTPServer
from Configuration import Configuration

from Web import Web
from FileSystem import FileSystem

class MoviesManager:
    def __init__(self):
        configuration = Configuration()
        port = int(configuration.config["port"])
        fileSystem = FileSystem()
        self.httpServer = HTTPServer(port, Web, fileSystem)
        
    def Start(self):
        self.httpServer.SmartMonitor()


if __name__ == '__main__':
    moviesManager = MoviesManager()
    moviesManager.Start()