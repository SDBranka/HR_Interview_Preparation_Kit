import unittest
import sys
sys.path.append("..")
from warm_up_challenges import sockMerchant


class test_sockMerchant(unittest.TestCase):
    def testOne(self):
        self.assertEqual(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]), 2)

    def testTwo(self):
        self.assertEqual(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]), 3)

    def testThree(self):
        self.assertEqual(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]), 2)


if __name__ == '__main__':
    unittest.main()      



#  #1 Sales by Match
# https://www.hackerrank.com/challenges/sock-merchant/problem
# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.

# Example
# n = 7
# ar = [1, 2, 1, 2, 1, 3, 2]

# There is one pair of color 1 and one of color 2. There are three 
# odd socks left, one of each color. The number of pairs is 2.

# Function Description
# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):
#     -int n: the number of socks in the pile
#     -int ar[n]: the colors of each sock

# Returns
#     -int: the number of pairs

# Input Format
# The first line contains an integer n, the number of socks represented 
# in ar. The second line contains n space-separated integers, ar[i], 
# the colors of the socks in the pile.

# Constraints
# -1 <= n <= 100
# 1 <= ar[i] <= 100 where 0 <= i <= n

# Sample Input
# STDIN                       Function
# -----                       --------
# 9                           n = 9
# 10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# Sample Output
# 3

# Example
# n = 7
# ar = [1, 2, 1, 2, 1, 3, 2]
# output = 2

# Example
# n = 9
# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# output = 3

# Complete the 'sockMerchant' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
