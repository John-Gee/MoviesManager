'''
Created on Jul 13, 2012

@author: john
'''
import unittest
from core.Configuration import Configuration


class ConfigurationTest(unittest.TestCase):
    def testCorrectPortSetup(self):
        configuration = Configuration()
        self.assertEqual('7060', configuration.config["port"])


if __name__ == "__main__":
    unittest.main()