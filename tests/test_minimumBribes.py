import unittest
from arrays import minimumBribes

class test_minimumBribes(unittest.TestCase):
    def testOne(self):
        self.assertEqual(minimumBribes([1, 2, 3, 5, 4, 6, 7, 8]), 1)

    def testTwo(self):
        self.assertEqual(minimumBribes([4, 1, 2, 3 ]), "Too chaotic" )

    def testThree(self):
        self.assertEqual(minimumBribes([2, 1, 5, 3, 4]), 3)
    
    def testFour(self):
        self.assertEqual(minimumBribes([2, 5, 1, 3, 4]), "Too chaotic")
    
    def testFive(self):
        self.assertEqual(minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]), "Too chaotic")
    
    def testSix(self):
        self.assertEqual(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]), 7)
    
    def testSeven(self):
        self.assertEqual(minimumBribes([1, 2, 5, 3, 4, 7, 8, 6]), 4)
    
    def testEight(self):
        self.assertEqual(minimumBribes([2, 3, 5, 4, 6, 7, 8, 1]), 8)


if __name__ == '__main__':
    unittest.main()       