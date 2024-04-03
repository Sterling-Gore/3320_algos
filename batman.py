from math import inf
import random
import math

num_crimes = []  
rest = [] 

def generate(m):
    for k in range(m):
        num_crimes.append(random.randint(1,15))
        rest.append(random.randint(1,math.ceil((m+2)/2)))


def max_crimes(m):
    cache = {}
    cache[-1] = 0
    path = []
    def MC(i):
        if i < 0:
            return 0
        if i not in cache:
            maxi = 0
            for k in range(i):
                if k + rest[k] + 1 == i:
                    temp = MC(k)
                    if maxi < temp:
                        maxi = temp
            include = num_crimes[i] + maxi
            exclude = MC(i-1)
            cache[i] = max(include, exclude)
            if include > exclude:
                path.append(i)
        return cache[i]
    ans = MC(m)
    print(f"MY PATH = {path}")
    for i in range(m+1):
        if i in cache:
            print(cache[i], end=" ")
        else:
            print("x ", end="")
    print()
    return ans
    

def Max_Crimes_Left(m): #Max crimes left, aka the value i represents nights left
    cache = {}
    cache[m] = num_crimes[m]
    path = []
    def MCL(i):
        if i > m:
            return 0
        if i not in cache:
            include = num_crimes[i] + MCL(i+1+rest[i])
            exclude = MCL(i+1)
            cache[i] = max(include, exclude)
            if include > exclude:
                path.append(i)
        return cache[i]
    ans = MCL(0)
    print(f"HOURANI PATH = {path}")
    return ans



days = 6
generate(days)
print(max_crimes(days-1))
print(Max_Crimes_Left(days-1))
print(num_crimes)
print(rest)