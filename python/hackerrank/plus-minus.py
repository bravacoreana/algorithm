#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p = 0
    z = 0
    n = 0
    value = float(1 / len(arr))
    for i in arr:
        if i > 0:
            p += value
        elif i == 0:
            z += value
        else:
            n += value
    print("{:.6f}".format(p))
    print("{:.6f}".format(n))            
    print("{:.6f}".format(z))            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
