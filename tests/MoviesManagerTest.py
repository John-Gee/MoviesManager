'''
Created on Jul 13, 2012

@author: john
'''
import unittest

import cherrypy

from core.MoviesManager import MoviesManager

class MoviesManagerTest(unittest.TestCase):
    def testCorrectPortSetup(self):
        moviesManager = MoviesManager()
        self.assertEqual(7060, moviesManager.httpServer.port)


if __name__ == "__main__":
    unittest.main()