#!/bin/python3

import math
import os
import random
import re
import sys

# runtime complexity: O(n) since we iterate overall the characters in s
# space complexity: O(1) additional space
# Complete the countingValleys function below.
def countingValleys(n, s):
    # n represents number of steps in gary hike
    # s represents the path

    valley_counter = 0
    altitude = 0
    for i in range(n):
        curr_char = s[i]
        if curr_char == 'U':
            altitude += 1
            if altitude == 0:
                valley_counter += 1
        else:
            altitude -= 1

    return valley_counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
