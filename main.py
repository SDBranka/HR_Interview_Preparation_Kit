import math
import os
import random
import re
import sys


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

#     int n: the number of socks in the pile
#     int ar[n]: the colors of each sock

# Returns

#     int: the number of pairs

# Input Format

# The first line contains an integer
# , the number of socks represented in .
# The second line contains space-separated integers, , the colors of the socks in the pile.

# Constraints

# -1<=n<=100
# 1<=ar[i]<=100 where 0<=i<=n

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


#!/bin/python3

# #
# # Complete the 'sockMerchant' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts following parameters:
# #  1. INTEGER n
# #  2. INTEGER_ARRAY ar
# #

def sockMerchant(n, ar):
    # sort the ar in increasing value
    for i in range(len(ar)):
        min = i
        for j in range(i+1, len(ar)):
            if ar[j] < ar[min]:
                ar[j], ar[min] = ar[min], ar[j]
    # get singular number occurences
    nums_in_ar = []
    nums_in_ar.append(ar[0])
    for i in range(len(ar)-1):
        if ar[i] != ar[i+1]:
            nums_in_ar.append(ar[i+1])
    # get count for singular number occurences
    count_for_nums = []
    for x in nums_in_ar:
        count = 0
        for ele in ar:
            if (ele == x):
                count = count + 1
        count_for_nums.append([x, count])
    # get number of pairs
    pairs_of_socks = 0
    for x in range(len(count_for_nums)):
        pairs_of_socks += math.floor(count_for_nums[x][1] / 2)
    
    return pairs_of_socks

# # Example
# n = 7
# ar = [1, 2, 1, 2, 1, 3, 2]
# print("@@@@@1")
# print(sockMerchant(n, ar))
# # output = 2

# # Example
# n = 9
# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# print("@@@@@2")
# print(sockMerchant(n, ar))
# output = 3

# #2
# An avid hiker keeps meticulous records of their hikes. During the 
# last hike that took exactly steps, for every step it was noted if 
# it was an uphill, U, or a downhill, D step. Hikes always start 
# and end at sea level, and each step up or down represents a 1 unit 
# change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, 
# starting with a step up from sea level and ending with a step down 
# to sea level. A valley is a sequence of consecutive steps below 
# sea level, starting with a step down from sea level and ending 
# with a step up to sea level.

# Given the sequence of up and down steps during a hike, find 
# and print the number of valleys walked through.

# Example
# steps = 8 path = [DDUUUUDD]

# The hiker first enters a valley 2 units deep. Then they climb 
# out and up onto a mountain 2 units high. Finally, the hiker 
# returns to sea level and ends the hike.

# Function Description
# Complete the countingValleys function in the editor below.
# countingValleys has the following parameter(s):
#     -int steps: the number of steps on the hike
#     -string path: a string describing the path

# Returns
#     int: the number of valleys traversed

# Input Format
# The first line contains an integer, the number 
# of steps in the hike. The second line contains 
# a single string, of characters that describe the path.

# Constraints
#  - 2<=steps<=10^6
# path[i] must be either U or D

# Sample Input
# 8
# UDDDUDUU

# Sample Output
# 1

# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    pos_y = 0
    times_in_valley = 0

    for i in range (len(path)):
        # if the user moves down decrease the y position user
        if path[i] == "D":
            pos_y -= 1
        # if the user moves up increase the y position of the user
        else:
            # if the user goes from below sea level to sea 
            # level (leaves a valley, thus has been in a valley) 
            # increase the number of times the user has been in a valley
            if pos_y == -1:
                times_in_valley += 1
            pos_y += 1

    return times_in_valley



# Example
# steps = 8 path = [DDUUUUDD]
steps = 8
path = "DDUUUUDD"
# path = "UDDDUDUU"
# path = ["D", "D", "U", "U", "U", "U", "D", "D"]
print(countingValleys(steps, path))

