num_nodes = 5
edges = [(0,1), (0,4), (1,2), (1,4), (1,5), (2, 3), (3, 4)]
print(num_nodes, len(edges))

#to create a class that represents a grapg as an adjacent list in python
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        #.edges - edges
        self.data = [[] for _ in range(num_nodes)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)


    #write a function to add, remove ane edge from a graph
    

graph1 = Graph(num_nodes, edges)
graph1.data