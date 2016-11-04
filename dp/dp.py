# -*- coding: utf-8 -*-

# my answer on StackOverflow: http://stackoverflow.com/questions/38930502/count-no-of-strings/38931819#38931819

__author__ = 'goran'

def get_count(s):
    N = len(s)
    # Initialize memoization matrix
    # First row all ones, all other zeros
    dp = list()
    dp.append([1] * N)
    for i in range(N - 1):
        dp.append([0] * N)

    # Convert characters to integers
    s = [ord(i) - ord('0') for i in s]

    for start in range(1, N):
        for end in range(start, N):
            for prev_start in range(0, start):
                if sum(s[prev_start:start]) <= sum(s[start:end+1]):
                    dp[start][end] += dp[prev_start][start - 1]

    return sum([dp[i][N - 1] for i in range(N)])

print(get_count('516'))

