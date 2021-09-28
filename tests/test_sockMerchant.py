import unittest
import sys
sys.path.append("..")
from warm_up_challenges import sockMerchant

class test_countingValleys(unittest.TestCase):
    def testOne(self):
        self.assertEqual(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]), 2)

    def testTwo(self):
        self.assertEqual(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]), 3)

    def testThree(self):
        self.assertEqual(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]), 2)


if __name__ == '__main__':
    unittest.main()       