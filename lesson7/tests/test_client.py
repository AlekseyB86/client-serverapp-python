import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))

from client import create_presence_message


class TestCreateMessage(unittest.TestCase):

    def testAccountNameLen(self):
        with self.assertRaises(ValueError):
            create_presence_message('Petrov1234567890123456789123')

    def testAccountNameType(self):
        with self.assertRaises(TypeError):
            create_presence_message(46346)

    def testDefaultUsername(self):
        self.assertEqual(create_presence_message()['user']['account_name'], "Guest")


if __name__ == "__main__":
    unittest.main()
