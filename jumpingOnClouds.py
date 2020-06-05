#!/bin/python3

import math
import os
import random
import re
import sys

# runtime complexity: O(n) since we iterate over all the values in the cloud list
# space complexity: O(1) additional space
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # c is an array of binary integers
    jump_counter = 0
    i = 0
    while i < len(c) - 1:
        if i + 2 == len(c) or c[i + 2] == 1:
            i += 1
            jump_counter+= 1
        else:
            i += 2
            jump_counter += 1
    
    return jump_counter
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
