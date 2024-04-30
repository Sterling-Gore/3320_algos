'''
  1110
  1011
  0011

  1233
  224
  2


  '''




#  n = 4
#  m = 3
matrix = [ [1,1,1,0], [1,0,1,1], [0,0,1,1]]

#base case when i = 0 and j - 0

#initialize the base case
cache = {(0,0) : matrix[0][0]}

for i in range(1,3):
    cache[(i,0)] = matrix[i][0] + cache[(i-1,0)]
for j in range(1,4):
    cache[(0,j)] = matrix[0][j]+ cache[(0,j-1)]


def topdown(i,j): 
    def MaxDirty(i,j):
        if (i,j) not in cache:
            cache[(i,j)] = matrix[i][j] + max(MaxDirty(i-1,j), MaxDirty(i, j-1))
        #print(cache[(i,j)])
        return cache[(i,j)]
    return MaxDirty(i,j)

def bottomup(n,m):
    def MaxDirty(n, m):
        tabulation = [[0 for _ in range(m)] for _ in range(n)]
        tabulation[0][0] = matrix[0][0]
        for i in range(1,n):
            tabulation[i][0] = tabulation[i-1][0] + matrix[i][0]
        for j in range(1,m):
            tabulation[0][j] = tabulation[0][j-1] + matrix[0][j]
        for i in range(1,n):
            for j in range(1, m):
                left = tabulation[i][j-1]  #if I move right from the left position
                up = tabulation[i-1][j] #if I move down from the up position
                tabulation[i][j] = max(left,up) + matrix[i][j]
        return tabulation[n-1][m-1]
        
    return MaxDirty(n,m)


print(topdown(2,3))  #this is len - 1
print(bottomup(3, 4)) #this is len
#off by one errors looool

def path(memo, n, m):
    pathline = []
    i = n
    j = m
    pathline.append(f"({n},{m})")
    while(pathline[-1] != f"({0},{0})"):
        if i == 0 and j == 0:
            pathline.append(f"({0},{0})")
        elif i == 0:
            pathline.append(f"({i},{j-1})")
            j = j-1
        elif j == 0:
            pathline.append(f"({i-1},{j})")
            i = i-1
        else:
            left = memo[(i-1,j)]
            up = memo[(i,j-1)]
            if memo[(i,j)] - matrix[i][j] == left:
                pathline.append(f"({i-1},{j})")
                i = i-1
            else:
                pathline.append(f"({i},{j-1})")
                j = j-1
    return pathline

print(path(cache, 2,3))
print("HIA")
        
        

for i in range(3):
    print(f"{cache[i,0]} {cache[i,1]} {cache[i,2]} {cache[i,3]}" )

