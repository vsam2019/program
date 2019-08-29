#!/bin/python

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxscore=scores[0]
    minscore=scores[0]
    maxcount =0
    mincount=0
    for i in range(len(scores)):
        if(scores[i]>maxscore):
            maxscore = scores[i]
            maxcount+=1
        if(scores[i]<minscore):
            minscore = scores[i]
            mincount+=1
    return [maxcount, mincount]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
