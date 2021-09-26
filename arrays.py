import math
import os
import random
import re
import sys

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

def hourglassSum(arr):
    max_sum = arr[0][0] + arr[0][1] + arr[0][2]\
                + arr[1][1]\
                + arr[2][0] + arr[2][1] + arr[2][2]

    for i in range(4):
        for j in range(4):
            sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]\
                + arr[i + 1][j + 1]\
                + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if sum > max_sum:
                max_sum = sum

    return max_sum



# #2 Arrays: Left Rotation
# https://www.hackerrank.com/challenges/ctci-array-left-rotation
# A left rotation operation on an array shifts each of the array's 
# elements 1 unit to the left. For example, if 2 left rotations 
# are performed on array [1, 2, 3, 4, 5], then the array would 
# become [3, 4, 5, 1, 2]. Note that the lowest index item moves 
# to the highest index in a rotation. This is called a circular array.

# Given an array a of n integers and a number, d, perform d left 
# rotations on the array. Return the updated array to be printed
#  as a single line of space-separated integers.

# Function Description
# Complete the function rotLeft in the editor below.
# rotLeft has the following parameter(s):
#     int a[n]: the array to rotate
#     int d: the number of rotations

# Returns
#     int a'[n]: the rotated array

# Input Format
# The first line contains two space-separated integers
# n and d, the size of a and the number of left rotations.
# The second line contains space-separated integers, each an a[i].

# Constraints
# 1 <= n <= 10^5
# 1 <= d <= n
# 1 <= a[i] <= 10^6

# Sample Input
# 5 4
# 1 2 3 4 5

# Sample Output
# 5 1 2 3 4

# Explanation
# When we perform d = 4 left rotations, the array
# undergoes the following sequence of changes:
# [1, 2, 3, 4, 5] ->
# [2, 3, 4, 5, 1] ->
# [3, 4, 5, 1, 2] ->
# [4, 5, 1, 2, 3] ->
# [5, 1, 2, 3, 4]


def rotLeft(a, d):

    # for i in range(d):
    #     hold = a[len(a) - 1]
    #     for j in range(len(a) - 1, -1, -1):
    #         if j > 0:
    #             temp = a[j - 1]
    #             a[j - 1] = hold
    #             hold = temp
    #         else: 
    #             a[len(a) - 1] = hold
    # return a

    n = len(a)
    a[:] = a[d:n] + a[0:d]
    return a



# # 3 New Year Chaos
# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen
# It is New Year's Day and people are in line for the 
# Wonderland rollercoaster ride. Each person wears a 
# sticker indicating their initial position in the queue 
# from 1 to n. Any person can bribe the person directly 
# in front of them to swap positions, but they still wear 
# their original sticker. One person can bribe at most 
# two others.

# Determine the minimum number of bribes that took 
# place to get to a given queue order. Print the number 
# of bribes, or, if anyone has bribed more than two people,
#  print Too chaotic.

# Example
# q ={1, 2, 3, 5, 4, 6, 7, 8}
# If person 5 bribes person 4, the queue will look 
# like this: 1, 2, 3, 5, 4, 6, 7, 8. Only 1bribe is 
# required. Print 1.

# q = [4, 1, 2, 3 ]
# Person 4 had to bribe 3 people to get to the 
# current position. Print Too chaotic.

# Function Description
# Complete the function minimumBribes in the editor below.

# minimumBribes has the following parameter(s):
#     int q[n]: the positions of the people after all bribes

# Returns
#     No value is returned. Print the minimum number of
#     bribes necessary or Too chaotic if someone has bribed 
#     more than 2 people.

# Input Format
# The first line contains an integer t, the number of 
# test cases.

# Each of the next t pairs of lines are as follows:
# - The first line contains an integer t, the number of 
#   people in the queue
# - The second line has n space-separated integers 
#   describing the final state of the queue.

# Constraints
# 1 <= t <= 10
# 1 <= n <= 10^5

# Subtasks

# For 60% score 1 <= n <= 10^3 
# For 100% score 1 <= n <= 10^5

# Sample Input

# STDIN       Function
# -----       --------
# 2           t = 2
# 5           n = 5
# 2 1 5 3 4   q = [2, 1, 5, 3, 4]
# 5           n = 5
# 2 5 1 3 4   q = [2, 5, 1, 3, 4]

# Sample Output

# 3
# Too chaotic

# Explanation

# Test Case 1

# The initial state:
# Ride- 1 2 3 4 5

# After person 5 moves one position ahead by bribing person 4:
# Ride- 1 2 3 5 4

# Now person 5 moves another position ahead by bribing person 3:
# Ride- 1 2 5 3 4

# And person 2 moves one position ahead by bribing person 1:
# Ride- 2 1 5 3 4

# So the final state is 2, 1, 5, 3, 4 after three
#  bribing operations.

# Test Case 2

# No person can bribe more than two people, yet it appears 
# person 5 has done so. It is not possible to achieve 
# the input state.

def minimumBribes(q):
    num_of_moves = 0
    for x in range(len(q)):
        if q[x] - 1 > 2 + x:
            return "Too chaotic"

        for j in range(max(0, q[x]-2), x):
            if q[j] > q[x]:
                num_of_moves += 1

    return num_of_moves
