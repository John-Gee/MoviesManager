'''
Created on Jul 13, 2012

@author: john
'''
import unittest

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


if __name__ == "__main__":
    unittest.main()