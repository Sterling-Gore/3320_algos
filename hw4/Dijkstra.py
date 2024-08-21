from math import inf


class binaryheap:
    def __init__(self):
        self.heap = []

    def heapify(self, index):
        if self.heap:
            min_index = index
            left = 2*index+1
            right = 2*index+2

            if left < self.size() and self.heap[left][1] < self.heap[min_index][1]:
                min_index = left
            if right < self.size() and self.heap[right][1] < self.heap[min_index][1]:
                min_index = right
            
            if (min_index != index):
                self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
                self.heapify(min_index)
                
    def push(self, val):
        self.heap.insert(0, val)
        self.heapify(0)
    def pop(self):
        if self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            self.heap = self.heap[:-1]
            self.heapify(0)
    def top(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    def size(self):
        return len(self.heap)
    def output(self):
        print(self.heap)


#dijkstra

#building out data 
#let's make a directed graph

#    source node :   [ (destination node,   edge weight), .... ]
adj_lists = {
    0 : [ (1,5), (3,7) ],
    1 : [ (2,3), (4,8) ],
    2 : [ (3,3) ],
    3 : [ (5,2) ],
    4 : [ (5,1) ],
    5 : [ (3,10) ]
}

    

def dijkstra(adj_list, root):
    heap = binaryheap()
    n = len(adj_list)
    dist = [inf] * n
    
    dist[root] = 0
    heap.push((root, 0))
    already_popped = []

    while heap.size() > 0 and len(already_popped) < n:
        u = heap.top()[0]
        heap.pop()
        already_popped.append(u)
        for nbr in adj_list[u]:
            old_distance = dist[nbr[0]]
            new_distance = dist[u] + nbr[1]  #remember nbr is a tuple (node, weight)
            if new_distance < old_distance:
                dist[nbr[0]] = new_distance
                heap.push((nbr[0], new_distance))
    print(dist)



dijkstra(adj_lists, 0)
    

    