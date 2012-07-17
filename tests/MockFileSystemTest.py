'''
Created on Jul 13, 2012

@author: john
'''
import unittest
from MockFileSystem import MockFileSystem

class MockFileSystemTest(unittest.TestCase):
        
    def testAddPathForGoodFolder(self):
        mockFileSystem = MockFileSystem()
        path = "goodFolder"
        self.assertFalse(path in mockFileSystem.paths, "The path has not yet been added.")
        mockFileSystem.AddPath(path, True)
        self.assertTrue(path in mockFileSystem.paths, "The path has been added.")
        self.assertTrue(path in mockFileSystem.dirs, "The path has been added as a dir.")
        
    def testAddPathForGoodFile(self):
        mockFileSystem = MockFileSystem()
        path = "goodFile"
        self.assertFalse(path in mockFileSystem.paths, "The path has not yet been added.")
        mockFileSystem.AddPath(path, False)
        self.assertTrue(path in mockFileSystem.paths, "The path has been added.")
        self.assertFalse(path in mockFileSystem.dirs, "The path has been added as a file.")
        
        
    def testAddPathForBadPath(self):
        mockFileSystem = MockFileSystem()
        path = "badPath"
        self.assertFalse(path in mockFileSystem.paths, "The path has not yet been added.")
        self.assertFalse(path in mockFileSystem.paths, "The path has not been added.")
        self.assertFalse(path in mockFileSystem.dirs, "The path has not been added as a folder or a file.")

    def testExistsForGoodFolder(self):
        mockFileSystem = MockFileSystem()
        path = "goodFolder"
        self.assertFalse(mockFileSystem.Exists(path), "The path has not yet been added.")
        mockFileSystem.AddPath(path, True)
        self.assertTrue(mockFileSystem.Exists(path), "The path has been added.")
        
    def testExistsForGoodFile(self):
        mockFileSystem = MockFileSystem()
        path = "goodFile"
        self.assertFalse(mockFileSystem.Exists(path), "The path has not yet been added.")
        mockFileSystem.AddPath(path, False)
        self.assertTrue(mockFileSystem.Exists(path), "The path has been added.")
        
    def testIsdirForGoodFolder(self):
        mockFileSystem = MockFileSystem()
        path = "goodFolder"
        self.assertFalse(mockFileSystem.IsDir(path), "The path has not yet been added.")
        mockFileSystem.AddPath(path, True)
        self.assertTrue(mockFileSystem.IsDir(path), "The folder has been added.")
        
    def testIsDirForGoodFile(self):
        mockFileSystem = MockFileSystem()
        path = "badPath"
        self.assertFalse(mockFileSystem.IsDir(path), "The path has not been added.")
        
    def testEmptyGetFolders(self):
        mockFileSystem = MockFileSystem()
        folders = mockFileSystem.GetSubFolders("")
        self.assertEquals(0, len(folders))
        
    def testGetFoldersGoodFoldersButPath(self):
        mockFileSystem = MockFileSystem()
        paths = ["path1", "path2", "path3"]
        for p in paths:
            mockFileSystem.AddPath(p, True)
            
        folders = mockFileSystem.GetSubFolders("notpath")
        self.assertEquals(0, len(folders))
        
    def testGetFoldersGoodFoldersGoodPath(self):
        mockFileSystem = MockFileSystem()
        paths = ["path1", "path2", "path3"]
        for p in paths:
            mockFileSystem.AddPath(p, True)
            
        folders = mockFileSystem.GetSubFolders("path")
        self.assertEquals(3, len(folders))

if __name__ == "__main__":
    unittest.main()