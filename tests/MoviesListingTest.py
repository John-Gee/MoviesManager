'''
Created on Jul 13, 2012

@author: john
'''
import unittest
from os import path
from core import MoviesListing
from MockFileSystem import MockFileSystem

class MoviesListingTest(unittest.TestCase):
    def setUp(self):
        self.moviesListing = MoviesListing.MoviesListing()
        self.mockFileSystem = MockFileSystem()

    def testFindMatchingFoldersInPathThrowsExceptionOnBadPath(self):
        badPath = "badPath"
        self.assertRaises(MoviesListing.BadPath, self.moviesListing.FindMatchingFoldersInPath, badPath, "", self.mockFileSystem)
        
    def testFindMatchingFoldersInPathThrowsExceptionOnFile(self):
        filePath = "filePath"
        self.mockFileSystem.AddPath(filePath, False)
        self.assertRaises(MoviesListing.NotADir, self.moviesListing.FindMatchingFoldersInPath, filePath, "", self.mockFileSystem)
        
    def testFindMatchingFoldersInPathReturnsGoodList(self):
        folderPath = "folderPath"
        self.mockFileSystem.AddPath(folderPath, True)
        folders = self.moviesListing.FindMatchingFoldersInPath(folderPath, ".*", self.mockFileSystem)
        self.assertEqual(1, len(folders))
        self.assertEqual(folderPath, folders[0])
        
    def testFindMatchingFoldersInPathWithNonMatchingRegExpReturnsGoodList(self):
        folderPath = "folderPath"
        self.mockFileSystem.AddPath(folderPath, True)
        folders = self.moviesListing.FindMatchingFoldersInPath(folderPath, "abcd.*", self.mockFileSystem)
        self.assertIsNone(folders)
        
    def testFindMatchingFoldersInPathWithMatchingRegExpReturnsGoodList(self):
        folderPath = "FolderPath"
        self.mockFileSystem.AddPath(folderPath, True)
        folders = self.moviesListing.FindMatchingFoldersInPath(folderPath, "Folder*", self.mockFileSystem)
        self.assertEqual(1, len(folders))
        self.assertEqual(folderPath, folders[0])


if __name__ == "__main__":
    unittest.main()