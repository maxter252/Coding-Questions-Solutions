#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    s_len = len(s)
    no_reps = n//s_len
    remainder = n % s_len
    remainder_count = 0
    count = 0
    for i, val in enumerate(s):
        if val == 'a':
            count += 1
            if i < remainder:
                remainder_count += 1
    
    return (count * no_reps) + remainder_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
