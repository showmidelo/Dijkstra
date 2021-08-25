class Router:

    def __init__(self, map_file_address):
        self.__edges = {}
        self.__vertices = []
        v = {}
        self.map_file_address = map_file_address

        # open the file and reading lines of it
        with open(map_file_address, 'r') as MAP:
            n, m = [int(i) for i in MAP.readline().split()]
        # reading vertex
            for i in range(n):
                identity, y, x = (float(i) for i in MAP.readline().split())
                identity = int(identity)
                vertex = Vertex(identity, y, x)
                self.__vertices.append(vertex)
                v[identity] = vertex
        # reading edges and add adjacent_vertices
            for i in range(m):
                id1, id2 = (int(i) for i in MAP.readline().split())
                edge = Edge(v[id1], v[id2])
                self.__edges[id1, id2] = edge
                self.__edges[id2, id1] = edge
                v[id1].adjacent_vertices.append(v[id2])
                v[id2].adjacent_vertices.append(v[id1])