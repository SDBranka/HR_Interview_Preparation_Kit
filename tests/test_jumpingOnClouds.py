import unittest
from warm_up_challenges import jumpingOnClouds

class test_jumpingOnClouds(unittest.TestCase):
    def testOne(self):
        self.assertEqual(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]), 3)

    def testTwo(self):
        self.assertEqual(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]), 4)

    def testThree(self):
        self.assertEqual(jumpingOnClouds([0, 0, 0, 0, 1, 0]), 3)
        
    def testFour(self):
        self.assertEqual(jumpingOnClouds([0, 0, 0, 1, 0, 0]), 3)

    def testFive(self):
        self.assertEqual(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]), 4)
    

if __name__ == '__main__':
    unittest.main()       