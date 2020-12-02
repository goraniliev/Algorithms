#!/bin/python3

"""
https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
"""

import math
import os
import random
import re
import sys


def count_smaller_or_equal(val, sorted_arr):
    if not sorted_arr:
        return 0

    # corner cases treatment, to simplify rest of the code
    if val >= sorted_arr[-1]:
        return len(sorted_arr)
    if val < sorted_arr[0]:
        return 0

    left, right = 0, len(sorted_arr)

    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] <= val:
            if mid == len(sorted_arr) - 1 or sorted_arr[mid + 1] > val:
                return mid + 1
            left = mid + 1
        else:
            # sorted_arr[mid] > val
            if mid == 0:
                return 1
            else:
                right = mid - 1


# Complete the triplets function below.
def triplets(a, b, c):
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    a.sort()
    c.sort()

    cnt = 0

    for i in b:
        cnt += count_smaller_or_equal(i, a) * count_smaller_or_equal(i, c)

    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()

    # used to test locally
    # counts = map(int, input().split(' '))
    # a = list(map(int, input().split(' ')))
    # b = list(map(int, input().split(' ')))
    # c = list(map(int, input().split(' ')))
    # print(triplets(a, b, c))