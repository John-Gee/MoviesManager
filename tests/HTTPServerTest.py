'''
Created on Jul 14, 2012

@author: john
'''
import threading
from cherrypy import process
from MockFileSystem import MockFileSystem
import time
import unittest
from core.HTTPServer import HTTPServer

class MockApplication(object):
    def __init__(self, obj, fileSystem):
        self.ready = False
        self.fileSystem = fileSystem
        
    def index(self):
        self.ready = True
        print "Mock ready"
    index.exposed = True

class HTTPServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.port = 12345
        self.applicationClass = MockApplication
        self.httpServer = HTTPServer(self.port, MockApplication, MockFileSystem())
        self.thread = threading.Thread(target=self.httpServer.SmartMonitor)
        self.thread.daemon = True
        self.thread.start()
        while not self.httpServer.ready:
            time.sleep(1)
        
        print "server is ready"
        time.sleep(1)

    def testInit(self):
        self.assertEqual(self.port, self.httpServer.port)
        self.assertEqual(self.applicationClass, self.httpServer.applicationClass)
        
    # cannot get the session to work yet
    def testGetAndSetSessionValue(self):
        key = "myKey"
        value = "myValue"
        #print "server is ready: {0}".format(self.httpServer.ready)
        #self.assertIsNone(self.httpServer.GetSessionValue(key), "The key is not yet in the session")
        #self.httpServer.SetSessionValue(key, value)
        #self.assertEqual(value, self.httpServer.GetSessionValue(key))
        
    def tearDown(self):
        process.bus.exit()
        unittest.TestCase.tearDown(self)

if __name__ == "__main__":
    unittest.main()