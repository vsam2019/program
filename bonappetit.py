#!/bin/python

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):

    #print k , b ,  bill

    bill.remove(bill[k])
    totalamt = sum(bill)
    annaamt = b - (totalamt/2) 

    if (totalamt/2) == b:
        print "Bon Appetit"
    else:
        print annaamt


if __name__ == '__main__':
    nk = raw_input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = map(int, raw_input().rstrip().split())

    b = int(raw_input().strip())

    bonAppetit(bill, k, b)
