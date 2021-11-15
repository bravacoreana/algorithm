#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    a = sorted(arr);
    minSum = a[0]+a[1]+a[2]+a[3]
    maxSum = a[-1]+ a[-2]+a[-3] + a[-4]
    print(minSum, maxSum)
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
