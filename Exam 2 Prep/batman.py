from math import inf
import random
import math
from functools import cache

num_crimes = []  
rest = [] 

def generate(m):
    for k in range(m):
        num_crimes.append(random.randint(1,15))
        rest.append(random.randint(1,math.ceil((m+2)/2)))


def max_crimes(m):
    @cache
    def MC(i):
        if i < 0:
            return 0ds
        else:
            include = num_crimes[i] + max((MC(k) for k in range(i) if k + rest[k] + 1 == i), default=-inf)
            exclude = MC(i - 1)
            return max(include, exclude)
    ans = MC(m)
    """print(f"MY PATH = {path}")
    for i in range(m+1):
        if i in cache:
            print(cache[i], end=" ")
        else:
            print("x ", end="")
    print()"""
    return ans
    

def Max_Crimes_Left(m): #Max crimes left, aka the value i represents nights left
    @cache
    def MCL(i):
        if i <= 0:
            return 0
        include = num_crimes[m-i] + MCL(i-1-rest[m-i])
        exclude = MCL(i-1)
        return max(include, exclude)
    ans = MCL(m)
    # print(f"HOURANI PATH = {path}")
    return ans



days = 1000
generate(days)
print(max_crimes(days-1))
print(Max_Crimes_Left(days-1))
# print(num_crimes)
# print(rest)