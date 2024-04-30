from math import inf

'''
def find(G, root):
    tree_edges = []
    visited = [False, False,...]
    DFSNUM = [0,0, ...]
    LOWNUM = [inf,inf,...]
    def DFS(u, count):
        visited[u] = True
        DFSNUM[u] = count
        for nbr in neighbors(u):
            if visited[nbr] == false:

'''
'''
def neighbors(u):
    if u == 'a':
        return ['c','e']
    if u == 'b':
        return ['c','d']
    if u == 'c':
        return ['a','b','d','e']
    if u == 'd':
        return ['b','c']
    if u == 'e':
        return ['a','c']
        '''


visited = {}
DFSNUM = {}
LOWNUM = {}
parent = {}
parent['a'] = None
count = 0
neighbors = {}
neighbors['a'] = ['b','c']
neighbors['b'] = ['a','c','d']
neighbors['c'] = ['a','b']
neighbors['d'] = ['b']

treeEdges = []
cutEdges = []



def dfs(u):
    print(u)
    global count 
    visited[u] = True
    DFSNUM[u] = count
    LOWNUM[u] = count
    count += 1
    for nbr in neighbors[u]:
        if nbr not in visited:
            treeEdges.append((u,nbr))
            parent[nbr] = u
            dfs(nbr) #anything that comes after this line in this instance will have all children calculated already. AKA I love recursion
            LOWNUM[u] = min(LOWNUM[u], LOWNUM[nbr])
            if LOWNUM[nbr] >= DFSNUM[u] and parent[u] != None:
                cutEdges.append( (u, nbr) )

        elif parent[u] != nbr:
            #backedge
            LOWNUM[u] = min(LOWNUM[u], DFSNUM[nbr])
            


dfs('a')
print('\n')
print(DFSNUM)
print(LOWNUM)
print(treeEdges)
print(cutEdges)


