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
        self.mockFileSystem = MockFileSystem()
        self.moviesListing = MoviesListing.MoviesListing(self.mockFileSystem)

    def testFindMatchingFoldersInPathThrowsExceptionOnBadPath(self):
        badPath = "badPath"
        self.assertRaises(MoviesListing.BadPath, self.moviesListing.FindMatchingFoldersInPath, badPath, "")
        
    def testFindMatchingFoldersInPathThrowsExceptionOnFile(self):
        filePath = "filePath"
        self.mockFileSystem.AddPath(filePath, False)
        self.assertRaises(MoviesListing.NotADir, self.moviesListing.FindMatchingFoldersInPath, filePath, "")
        
    def testFindMatchingFoldersInPathReturnsGoodList(self):
        folderPath = "folderPath"
        self.mockFileSystem.AddPath(folderPath, True)
        folders = self.moviesListing.FindMatchingFoldersInPath(folderPath, ".*")
        self.assertEqual(1, len(folders))
        self.assertEqual(folderPath, folders[0])
        
    def testFindMatchingFoldersInPathWithNonMatchingRegExpReturnsGoodList(self):
        folderPath = "folderPath"
        self.mockFileSystem.AddPath(folderPath, True)
        folders = self.moviesListing.FindMatchingFoldersInPath(folderPath, "abcd.*")
        self.assertIsNone(folders)
        
    def testFindMatchingFoldersInPathWithMatchingRegExpReturnsGoodList(self):
        folderPath = "FolderPath"
        self.mockFileSystem.AddPath(folderPath, True)
        folders = self.moviesListing.FindMatchingFoldersInPath(folderPath, "Folder*")
        self.assertEqual(1, len(folders))
        self.assertEqual(folderPath, folders[0])
        
    def testMatchedFoldersDoesNotReturnFiles(self):
        folderPath = "FolderPath"
        filePath = "FilePath"
        otherFolderPath = "OtherFolderPath"
        self.mockFileSystem.AddPath(folderPath, True)
        self.mockFileSystem.AddPath(folderPath + "/" + filePath, False)
        self.mockFileSystem.AddPath(folderPath + "/" + otherFolderPath, True)
        folders = self.moviesListing.FindMatchingFoldersInPath(folderPath, "Folder*")
        self.assertEqual(2, len(folders))
        self.assertEqual(folderPath, folders[0])

if __name__ == "__main__":
    unittest.main()