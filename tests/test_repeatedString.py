import unittest
import sys
sys.path.append("..")
from warm_up_challenges import repeatedString

class test_repeatedString(unittest.TestCase):
    def testOne(self):
        self.assertEqual(repeatedString("abcac", 10), 4)

    def testTwo(self):
        self.assertEqual(repeatedString("aba", 10), 7)

    def testThree(self):
        self.assertEqual(repeatedString("a", 1000000000000), 1000000000000)
        
    def testFour(self):
        self.assertEqual(repeatedString("x","21342424"), 0)

    def testFive(self):
        self.assertEqual(repeatedString("kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm", 736778906400), 51574523448)
    
    def testSix(self):
        self.assertEqual(repeatedString("ababa", 3), 2)




if __name__ == '__main__':
    unittest.main()       