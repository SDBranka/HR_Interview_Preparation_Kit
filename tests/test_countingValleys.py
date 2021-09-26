import unittest
from warm_up_challenges import countingValleys

class test_countingValleys(unittest.TestCase):
    def testOne(self):
        self.assertEqual(countingValleys(8, "DDDUUUUDD"), 1)

    def testTwo(self):
        self.assertEqual(countingValleys(8, "UDDDUDUU"), 1)


if __name__ == '__main__':
    unittest.main()       