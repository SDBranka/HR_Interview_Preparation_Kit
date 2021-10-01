import unittest
import sys
sys.path.append("..")
from arrays import hourglassSum


class test_hourglassSum(unittest.TestCase):
    def testOne(self):
        self.assertEqual(hourglassSum([
                                    [-9, -9, -9, 1, 1, 1],
                                    [0, -9, 0, 4, 3, 2],
                                    [-9, -9, -9, 1, 2, 3],
                                    [0, 0, 8, 6, 6, 0],
                                    [0, 0, 0, -2, 0, 0],
                                    [0, 0, 1, 2, 4, 0]
                                    ]),
                                    28 )

    def testTwo(self):
        self.assertEqual(hourglassSum([
                                    [-1, -1, 0, -9, -2, -2],
                                    [-2, -1, -6, -8, -2, -5],
                                    [-1, -1, -1, -2, -3, -4,],
                                    [-1, -9, -2, -4, -4, -5],
                                    [-7, -3, -3, -2, -9, -9],
                                    [-1, -3, -1, -2, -4, -5]
                                    ]),
                                    -6 )

    def testThree(self):
        self.assertEqual(hourglassSum([
                                    [1, 1, 1, 0, 0, 0],
                                    [0, 1, 0, 0, 0, 0],
                                    [1, 1, 1, 0, 0, 0],
                                    [0, 0, 2, 4, 4, 0],
                                    [0, 0, 0, 2, 0, 0],
                                    [0, 0, 1, 2, 4, 0]
                                    ]),
                                    19 )

if __name__ == '__main__':
    unittest.main()       



#  #1 2D Array - DS
# https://www.hackerrank.com/challenges/2d-array
# Given a 6x6 2D Array, arr:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# An hourglass in A is a subset of values with indices 
# falling in this pattern in arr's graphical representation:
# a b c
#   d
# e f g

# There are 16 hourglasses in arr. An hourglass sum is the sum
# of an hourglass' values. Calculate the hourglass sum for 
# every hourglass in , then print the maximum hourglass sum. 
# The array will always be 6 x 6.

# Example
# arr = 
# -9 -9 -9  1 1 1 
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0

# The 16 hourglass sums are:
# -63, -34, -9, 12, 
# -10,   0, 28, 23, 
# -27, -11, -2, 10, 
#   9,  17, 25, 18

# The highest hourglass sum is 28 from 
# the hourglass beginning at row 1, column 2:
# 0 4 3
#   1
# 8 6 6

# Note: If you have already solved the Java 
# domain's Java 2D Array challenge, you may 
# wish to skip this challenge.

# Function Description
# Complete the function hourglassSum in the editor below. 
# hourglassSum has the following parameter(s):
#     int arr[6][6]: an array of integers

# Returns
#     int: the maximum hourglass sum

# Input Format
# Each of the 6 lines of inputs arr[i] 
# contains 6 space-separated integers arr[i][j].

# Constraints
    # -9 <= arr[i][j] <= 9
    # 0 <= i, j <= 5

# Output Format
# Print the largest (maximum) hourglass 
# sum found in arr.

# Sample Input
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

# Sample Output
# 19

# Explanation
# contains the following hourglasses:

# 111 110 100 000
#  1   0   0   0 
# 111 110 100 000
# 
# 010 100 000 000
#  1   1   0   0 
# 002 024 244 440
# 
# 111 110 100 000
#  0   2   4   4
# 000 002 020 200
# 
# 002 024 244 440
#  0   0   2   0 
# 001 012 124 240

# The hourglass with the maximum sum (19) is:
# 2 4 4
#   2
# 1 2 4

# Complete the 'hourglassSum' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# # as a 1d array
# def hourglassSum(arr):
#     # Write your code here
#     max_sum = 0
#     for i in range(22):
#         sum = arr[i] + arr[i + 1] + arr[i + 2]\
#             + arr[i + 7] + arr[i + 12] + arr[i + 13]\
#             + arr[i + 14]
#         if sum > max_sum:
#             max_sum = sum
#     return max_sum


