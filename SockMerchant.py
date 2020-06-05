import math
import os
import random
import re
import sys

# runtime complexity: O(n) for iterating over all the different socks
# space complexity: O(n) additional space for the dictionary and the set of socks
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # n represents the number of socks
    # arr contains all the socks

    sock_map = {}
    sock_set = set(ar)
    counter = 0

    # update the sock map
    for sock in ar:
        if sock not in sock_map:
            sock_map[sock] = 1
        else:
            value = sock_map[sock]
            value += 1
            sock_map[sock] = value
    
    for sock in sock_set:
            counter += sock_map[sock] // 2
    
    return counter




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
