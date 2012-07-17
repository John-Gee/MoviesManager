'''
Created on Jul 13, 2012

@author: john
'''
import unittest

import os
import sys
from os import path

from core.FileSystem import FileSystem

class FileSystemTest(unittest.TestCase):
    def setUp(self):
        self.fileSystem = FileSystem()
    
    def testExistReturnsTrueWhenPathExists(self):
        self.assertTrue(self.fileSystem.Exists(path.curdir))
    def testExistReturnsFalseWhenPathDoesNotExist(self):
        self.assertFalse(self.fileSystem.Exists(path.join(path.curdir, "  " , path.curdir)))

    def testIsDirReturnsTrueWhenPathIsADir(self):
        self.assertTrue(self.fileSystem.IsDir(path.curdir))
    def testIsDirReturnsFalseWhenPathIsNotADir(self):
        self.assertFalse(self.fileSystem.IsDir(path.join(path.curdir, __file__)))

    def testGetSubFolders(self):
        path = os.path.dirname(__file__)
        folders = self.fileSystem.GetSubFolders(path)
        self.assertFalse(__file__ in folders)

    def testCompleteReturnsNoneWhenNoMatch(self):
        matches = self.fileSystem.Complete("/a/b/c/d/e/f")
        self.assertEqual([], matches)
        
    def testCompleteReturnsCorrectPathsWhenMatched(self):
        #If the module is executed as a script __name__ will be '__main__' and sys.argv[0] will be the full path of the module.
        if __name__ == '__main__':
            modulePath = os.path.split(sys.argv[0])[0]
        #Else the module was imported and it has a __file__ attribute that will be the full path of the module.
        else:
            modulePath = os.path.split(__file__)[0]   
        
        baseFolder = os.path.dirname(modulePath)
        reducedBaseFolder = baseFolder[:-2]
        matches = self.fileSystem.Complete(reducedBaseFolder)
        print baseFolder
        print reducedBaseFolder
        print matches
        self.assertEqual(1, len(matches))
        self.assertEqual(baseFolder, matches[0])

if __name__ == "__main__":
    unittest.main()