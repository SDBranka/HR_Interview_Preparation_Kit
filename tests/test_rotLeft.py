import unittest
from arrays import rotLeft

class test_rotLeft(unittest.TestCase):
    def testOne(self):
        self.assertEqual(rotLeft([1, 2, 3, 4, 5], 4), [5, 1, 2, 3, 4])

    def testTwo(self):
        self.assertEqual(rotLeft([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])
    

if __name__ == '__main__':
    unittest.main()       