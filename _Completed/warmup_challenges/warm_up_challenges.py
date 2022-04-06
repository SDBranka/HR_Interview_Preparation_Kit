import math
import os
import random
import re
import sys


# 1
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


# 2
def countingValleys(steps, path):
    # Write your code here
    pos_y = 0
    times_in_valley = 0

    for i in range(len(path)):
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


# 3
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


# 4
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
