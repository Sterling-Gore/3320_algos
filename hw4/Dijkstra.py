from math import Inf

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

#shortest_paths = [Inf] * len(adj_lists)

min_heap = []
index = [10,5,6,7,3,4,2,1]


class binaryheap:
    def __init__(self):
        self.heap = []

    def heapify(self, ):
        if self.heap:
            
            
        


    def push(self, val):
        self.heap.append(val)
        self.heapify()
    def pop(self):
        self.heap = self.heap[1:]
        self.heapify()
    def top(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    def size(self):
        return len(self.heap)
    def output(self):
        print(self.heap)

    
    