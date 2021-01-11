class Graph:
    def __init__(self):

        self._adjacency_list = {}

    def add_node(self,value):

        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):

        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not in graph")

        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not in graph")

    def get_nodes(self):
        return self._adjacency_list.keys()

    def size(self):
        return len(self._adjacency_list)

    def get_neighbors(self):
        


class Vertex:
    def __init__(self, value):

        self.value = value

class Edge:
    pass


