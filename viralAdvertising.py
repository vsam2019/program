#!/bin/python

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):

    persons = 5
    listli =[]
    for i in range(1,n + 1):
        
        like = persons//2
        persons = like * 3
        listli.append(like)
    return sum(listli)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
