#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    
    num_five = n
    
    while num_five % 3 != 0:
        num_five -= 5
    if num_five < 0:
        print(-1)
    else: 
        num_three = n - num_five
        print('5' * num_five + '3' * num_three)
        
        
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
