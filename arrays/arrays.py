import math
import os
import random
import re
import sys


# 1
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


# 2
def rotLeft0(a, d):
    for i in range(d):
        hold = a[len(a) - 1]
        for j in range(len(a) - 1, -1, -1):
            if j > 0:
                temp = a[j - 1]
                a[j - 1] = hold
                hold = temp
            else: 
                a[len(a) - 1] = hold
    return a

def rotLeft1(a, d):
    n = len(a)
    a[:] = a[d:n] + a[0:d]
    return a


# 3
def minimumBribes(q):
    num_of_moves = 0
    for x in range(len(q)):
        # print(f"_x = {x}")
        if q[x] - 1 > 2 + x:
            return "Too chaotic"

        # print(f"x = {x}")
        # print(f"q[{x}]- 2 = {q[x] - 2}")
        # print(f"max = {max(0, q[x]-2)}")
        for j in range(max(0, q[x]-2), x):
            # print(f"q[{x}] = {q[x]}")
            # print(f"j = {j}")
            # print(f"x = {x}")
            # print(f'q[{j}]  = {q[j]}')
            if q[j] > q[x]:
                # print("moves +1")
                num_of_moves += 1
            # print("after the if")

    return num_of_moves


#4
# too slow    
def minimumSwaps0(arr):
    swaps = 0

    for i in range(len(arr)):
        if arr[i] != i + 1:
            temp = arr.index(i + 1)
            arr[i], arr[temp] = arr[temp], arr[i]
            swaps += 1
        # print(f"arr{i} = {arr}")
    return swaps

def minimumSwaps(arr):
    swaps = 0
    #iterate over entire array
    for i in range(0,len(arr)):
        while arr[i] != (i+1):
            #temp is the correct index of arr[i]
            temp = arr[i]-1
            #swap this with whatever element is where arr[temp] is, this will
            #continue to swap until arr[i] == index+1
            arr[i], arr[temp] = arr[temp], arr[i]
            #increase swaps
            swaps+=1
    return swaps


# 5