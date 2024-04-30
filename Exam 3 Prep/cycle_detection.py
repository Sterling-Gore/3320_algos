
nodes = [1,2,3,4,5,6,7,8]
neighbors = {}
neighbors[1] = [2,3,5]
neighbors[2] = [1,4]
neighbors[3] = [1,8]
neighbors[4] = [2,5,6]
neighbors[5] = [1,4,6]
neighbors[6] = [4,5,7]
neighbors[7] = [6,8]
neighbors[8] = [3,7]


def cycle_detection(nodes):
    visited = {}
    parent = {}
    stack = []
    backedges = []
    cycle = [0]* (len(nodes)+1)

    def DFS(v):
        nonlocal backedges
        nonlocal cycle
        nonlocal stack
        visited[v] = True
        stack.append(v)
        for nbr in neighbors[v]:
            if nbr not in visited:
                parent[nbr] = v
                DFS(nbr)
            elif parent[v] != nbr: #this mean there's a back edge
                backedge = {v,nbr}
                if backedge not in backedges:
                    backedges.append( backedge )
                    temp_cycle = stack[stack.index(nbr):]
                    if len(cycle) > len(temp_cycle):
                        cycle = temp_cycle  
        stack = stack[:-1] #pop

    for i in nodes:
        if i not in visited:
            k = i+3
            if k <= 8:
                parent[k] = None
                DFS(k)
            else:
                parent[k - 8] = None
                DFS(k - 8)
    print(cycle)

cycle_detection(nodes)

            
