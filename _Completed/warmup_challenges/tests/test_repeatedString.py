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



# #4 Repeated String
# https://www.hackerrank.com/challenges/repeated-string/problem
# There is a string, s, of lowercase English letters that 
# is repeated infinitely many times. Given an integer, n, 
# find and print the number of letter a's in the first n 
# letters of the infinite string.

# Example
# s = 'abcac'
# n = 10

# The substring we consider is abcacabcac, the first 10 
# characters of the infinite string. There are 4 occurrences 
# of a in the substring.

# Function Description
# Complete the repeatedString function in the editor below.
# repeatedString has the following parameter(s):
#     s: a string to repeat
#     n: the number of characters to consider

# Returns
#     int: the frequency of a in the substring

# Input Format
# The first line contains a single string, s.
# The second line contains an integer, n.

# Constraints
#      1 <= |s| <= 100
#      1 <= n <= 10^12
#      For 25% of the test cases, n <= 10^6.

# Sample Input 0
# aba
# 10
# Sample Output 0
# 7
# Explanation 0
# The first n = 10 letters of the infinite string are 
# abaabaabaa. Because there are 7 a's, we return 7.

# Sample Input 1
# a
# 1000000000000
# Sample Output 1
# 1000000000000
# Explanation 1
# Because all of the first n = 1000000000000 letters 
# of the infinite string are a, we return 1000000000000
