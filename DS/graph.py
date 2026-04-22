class Graph:
    def __init__(self):
        # what data structure?
        self.graph = {}

    def add_vertex(self, node):
        if node in self.graph:
            return
        self.graph[node] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
       
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(u)

        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)
    

    def remove_vertex(self, node):
        if node in self.graph:
            return None
        for neighbour in self.graph:
            self.graph[neighbour].remove(node)
        del self.graph[node]

    def has_edge(self, u, v):
        return u in self.graph and v in self.graph[u]

    def get_neighbors(self, node):
        return self.graph.get(node, [])
        