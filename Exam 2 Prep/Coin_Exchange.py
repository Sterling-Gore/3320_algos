from math import inf

def Min_Coin(coins, target):
    cache = {0:0}
    
    
    def MC(t):
        if t < 0:
            return inf
        if t not in cache:
            mini = inf
            for x in coins:
                m = MC(t- x)
                if mini > m:
                    mini = m
            cache[t] = 1 + mini
        return cache[t]
    print( MC(target) )
    
    # for i in range(len(coins)+1):
    #     for j in range(T+1):
    #         if (i,j) in cache:
    #             print(f"{cache[(i,j)]} ", end = "")
    #         else:
    #             print("x ", end="")
    #     print()
    return MC(target)
    


li = [12, 3]
Min_Coin(li, 9)