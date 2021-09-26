import math
import os
import random
import re
import sys


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



# #2 Counting Valleys
# https://www.hackerrank.com/challenges/counting-valleys
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
#  - 2 <= steps <= 10^6
# path[i] must be either U or D

# Sample Input
# 8
# UDDDUDUU
# Sample Output
# 1

# Complete the 'countingValleys' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path

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



# #3 Jumping on the Clouds
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
# There is a new mobile game that starts with consecutively 
# numbered clouds. Some of the clouds are thunderheads and others 
# are cumulus. The player can jump on any cumulus cloud having a 
# number that is equal to the number of the current cloud plus 
# 1 or 2. The player must avoid the thunderheads. Determine 
# the minimum number of jumps it will take to jump from the 
# starting postion to the last cloud. It is always possible to 
# win the game.
# For each game, you will get an array of clouds numbered 0
# if they are safe or 1 if they must be avoided.

# Example
# c = [0, 1, 0, 0, 0, 1, 0]
# Index the array from 0...6. The number on each cloud is its 
# index in the list so the player must avoid the clouds at 
# indices 1 and 5. They could follow these two 
# paths: 0->2->4->6 or 0->2->3->4->6. The first path takes 
# 3 jumps while the second takes 4. Return 3.

# Function Description
# Complete the jumpingOnClouds function in the editor below. 
# jumpingOnClouds has the following parameter(s):

#     -int c[n]: an array of binary integers

# Returns

#     -int: the minimum number of jumps required

# Input Format

# The first line contains an integer n, the total number
# of clouds. The second line contains n space-separated 
# binary integers describing clouds c[i] where 0 <= i < n.

# Constraints

# - 2 <= n <= 100
# - c[i] is either 0 or 1
# - c[0] = c[n-1] = 0

# Output Format
# Print the minimum number of jumps needed to win the game.

# Sample Input 0
# 7
# 0 0 1 0 0 1 0

# Sample Output 0
# 4

# Explanation 0:
# The player must avoid c[2] and c[5]. The game can be won
# with a minimum of 4 jumps:

# Sample Input 1
# 6
# 0 0 0 0 1 0

# Sample Output 1
# 3

# Explanation 1:
# The only thundercloud to avoid is c[4]. The game can be won 
# in 3 jumps:

# Complete the 'jumpingOnClouds' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.

def jumpingOnClouds(c):
    position = 0
    jumps = 0
    while position < len(c)-1:
        if position < len(c) - 2 and c[position + 2] == 0:
            jumps += 1
            position += 2
        else:
            jumps += 1
            position += 1        

    return jumps



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

def repeatedString(s, n):
    s_len = len(s)
    count = 0
    if s_len == 0:
        count = 0
    elif s_len == 1:
        if s[0] == 'a':
            count = n
        else:
            count = 0
    else:
        if n > s_len:
            # get the number of a's in s
            num_a_in_s = 0
            for ele in s:
                if (ele == 'a'):
                    num_a_in_s += 1
            # get the number of times s fits fully into n
            num_of_times_s = n // s_len
            # set count to equal the number of a's in s * the number of times s will be used
            count = num_a_in_s * num_of_times_s
            # work with the remaining number of letters
            num_to_check = s_len * num_of_times_s
            num_letters_to_add = n - num_to_check
            for letter in range(num_letters_to_add):
                if s[letter] == 'a':
                    count += 1
        elif n < s_len:
            for letter in range(n):
                if s[letter] == 'a':
                    count += 1
    return count