'''
Created on Jul 12, 2012

@author: john
'''

from HTTPServer import HTTPServer
from Configuration import Configuration

from HelloWorld import HelloWorld

class MoviesManager:
    def __init__(self):
        configuration = Configuration()
        port = int(configuration.config["port"])
        self.httpServer = HTTPServer(port, HelloWorld)
        
    def Start(self):
        self.httpServer.SmartMonitor()


if __name__ == '__main__':
    moviesManager = MoviesManager()
    moviesManager.Start()