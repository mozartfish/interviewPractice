mport math
import os
import random
import re
import sys
from collections import Counter

# runtime complexity: O(n) for python count function
# space complexity: O(1) additional space
# Complete the repeatedString function below.
def repeatedString(s, n):
    q1 = n // len(s)
    x=s.count('a')
    x1 = q1 * x
    x2 = s[:n % len(s)].count('a')

    return x1 + x2


    # new_string = s * n
    # count_map = Counter(new_string)
    # return count_map['a']

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
