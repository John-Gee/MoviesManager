'''
Created on Jul 14, 2012

@author: john
'''
import os
import sys
import cherrypy

class HTTPServer(object):
    def __init__(self, port, applicationClass, fileSystem):
        self.port = port
        self.applicationClass = applicationClass
        self.application = None
        self.fileSystem = fileSystem
        self.ready = False
        
    def SmartMonitor(self):
        self.application = self.applicationClass(self, self.fileSystem)
        
        #If the module is executed as a script __name__ will be '__main__' and sys.argv[0] will be the full path of the module.
        if __name__ == '__main__':
            modulePath = os.path.split(sys.argv[0])[0]
        #Else the module was imported and it has a __file__ attribute that will be the full path of the module.
        else:
            modulePath = os.path.split(__file__)[0]          
        
        cherryConfig = { 'global': 
            {
                'server.socket_port'            : self.port,
                'server.socket_host'            : '0.0.0.0',
                'server.thread_pool'            : 10,
                'tools.sessions.on'             : True,
                'tools.sessions.storage_type'   : 'ram',
                'tools.sessions.timeout'        : 5000,
                'tools.staticdir.root'          : os.path.dirname(modulePath)
            },
                        '/javascript':
            {
                'tools.staticdir.on'            : True,
                'tools.staticdir.dir'           : "javascript"
            },
                        '/style':
            {
                'tools.staticdir.on'            : True,
                'tools.staticdir.dir'           : "style"
            }
        }
        
        cherrypy.config.update(cherryConfig)
        cherrypy.log.screen = True
        
        cherrypy.tree.mount(self.application, '', cherryConfig)
        cherrypy.engine.autoreload = True
        
        if hasattr(cherrypy.engine, 'signal_handler'):
            cherrypy.engine.signal_handler.handlers["SIGINT"]= cherrypy.engine.signal_handler.bus.exit
            cherrypy.engine.signal_handler.subscribe()
        
        print "Web server started"
        cherrypy.engine.start()
        self.ready = True
        cherrypy.engine.block()
        print "Web server stopped"
        self.ready = False
        
    def GetSessionValue(self, key):
        print "web server is ready: {0}".format(self.ready)
        return cherrypy.session.get(key)
    
    def SetSessionValue(self, key, value):
        cherrypy.session[key] = value