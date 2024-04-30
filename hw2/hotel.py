#hotel
#[0,4,4,14, 4, 28 ]
#[100,0,1,5, 3, 14]
#[100,100,0,10, 5, 13]
#[100,100,100,0, 3, 8]
#[100,100,100,100,0, 12]
#[100,100,100,100,100,0]
penalty = [[100,4,4,14, 4, 28 ],[100,100,1,5, 3, 14],[100,100,100,10, 5, 13],[100,100,100,100, 3, 8],[100,100,100,100,100, 12],[100,100,100,100,100,100]]

cache = {}
for j in range(1, len(penalty)):
    i = j-1
    cache[(i,j)] = penalty[i][j]
path = []
def min_cost(i,j):
    if (i,j) not in cache:
        minum = penalty[i][j]
        path.append((i,j))
        
        for k in range(i+1, j):
            mc = min_cost(i,k) + min_cost(k,j)
            if minum > mc:
                minum = mc 
                path[-1] = (i,k,j)
        cache[(i,j)] =  minum
    return cache[(i,j)]

print(min_cost(0,5))


def bottom_up(n):
    tabulation = {}
    for i in range(1,n):
        tabulation[(i-1,i-1)] = 0 
        tabulation[(i-1,i)] = penalty[i-1][i]

    for l in range(1, n-1):
        for j in range(n-l,n):
            i = n-(l+2)
            tabulation[(i,j)] = penalty[i][j]
            for k in range(i+1,j):
                mc_path = tabulation[(i,k)] + tabulation[(k,j)]
                if mc_path < tabulation[(i,j)]:
                    tabulation[(i,j)] = mc_path

    for i in range(n):
        for j in range(n):
            if (i,j) in tabulation:
                print(f"{tabulation[(i,j)]} ", end="")
            else:
                print('x ', end="")
        print()
            
    return tabulation[(0,n-1)]


print(bottom_up(6))

'''
n = 4
for l in range(1, n-1):
    for j in range(n-l, n):
        i = n-l-2
        print(f"({i},{j}), or ", end = "")
        for k in range(i+1, j):
            print(f"({i},{k}) + ({k},{j}), or ", end = "")
        print()
        
       ''' 
