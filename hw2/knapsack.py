import random
import timeit


class item():
    def __init__(self, weight, profit):
        self.weight =  weight
        self.profit = profit


def top_down_KS(items, MaxW):
    cache = {}
    cache[(0,0)] = 0
    for w in range(1, MaxW + 1):
        if items[0].weight <= w:
            cache[(0,w)] = items[0].profit
        else:
            cache[(0,w)] = 0
    for i in range(1, len(items)):
        cache[(i,0)] = 0
    
    def helper(i, W):
        if W < 0:
            return 0
        if (i,W) not in cache:
            include = 0
            if W - items[i].weight >= 0:
                include = items[i].profit + helper(i-1, W - items[i].weight)
            exclude = helper(i-1, W)
            cache[(i,W)] = max(include, exclude)
        return cache[(i,W)]

    return helper(len(items)-1, MaxW) 
    




def bottom_up_KS(items, MaxW):
    tabulation = [[0 for _ in range(MaxW+1)] for _ in range(len(items))]
    tabulation[0][0] = 0

    for w in range(1, MaxW+1):
        if items[0].weight <= w:
            tabulation[0][w] = items[0].profit
        else:
            tabulation[0][w] = 0
    
    for i in range(1, len(items)):
        tabulation[i][0] = 0
    
    for i in range(1, len(items)):
        for w in range(1, MaxW+1):
            include = 0
            if w - items[i].weight >= 0:
                include = items[i].profit + tabulation[i-1][w - items[i].weight]
            exclude = tabulation[i-1][w]
            tabulation[i][w] = max(include, exclude)
    
    return tabulation[len(items)-1][MaxW]
    
    

 
def item_generator(n):
    items = []
    for i in range(n):
        #weight, profit
        new_item = item(random.randint(1,20), random.randint(1,50))
        items.append(new_item)
    return items


def main():
    number_of_items = 256
    items = item_generator(number_of_items)
    max_weight = 100

    start_time_top_down = timeit.default_timer()
    TD_solution = top_down_KS(items, max_weight)
    final_time_top_down = timeit.default_timer() - start_time_top_down


    start_time_bottom_up = timeit.default_timer()
    BU_solution =  bottom_up_KS(items, max_weight)
    final_time_bottom_up = timeit.default_timer() - start_time_bottom_up


    print( f"Top down: {final_time_top_down} seconds.              Solution: {TD_solution}")
    print( f"Bottom up: {final_time_bottom_up} seconds.              Solution: {BU_solution}")



if __name__ == "__main__":
    main()