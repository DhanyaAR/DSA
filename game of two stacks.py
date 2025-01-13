#!/bin/python3

import math
import os
import random
import re
import sys

def twoStacks(maxSum, a, b):
    count=0
    sum=0
    i=0
    j=0
    while i < len(a) and sum + a[i] <= maxSum:
        sum+=a[i]
        i+=1
        count+=1 
    max_cnt=count
    while j<len(b):
        sum+=b[j]
        j+=1
        while sum > maxSum and i > 0:
            i -= 1
            sum -= a[i]
        if sum <= maxSum:
            max_cnt = max(max_cnt, i + j)
    return max_cnt
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
