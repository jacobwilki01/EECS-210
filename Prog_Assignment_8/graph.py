class Graph:
    def __init__(self, edges, name=""):
        self.vertices = []
        self.edges = []
        self.circuit = []
        self.name = name

        #Clean up vertices
        for edge in edges:
            self.vertices.append(edge[0])
            self.vertices.append(edge[1])
        
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        for x in range(0,len(self.vertices)):
            self.vertices[x] = Vertex(self.vertices[x])

        #Clean up edges
        for edge in edges:
            self.edges.append(Edge(edge[0], edge[1]))
        
        for edge in self.edges:
            for vertex in self.vertices:
                if edge.pair[0] == vertex.label:
                    edge.pair = (vertex, edge.pair[1])
                elif edge.pair[1] == vertex.label:
                    edge.pair = (edge.pair[0], vertex)

        #Clean up Vertex Neighbors
        for vertex in self.vertices:
            for edge in self.edges:
                if vertex == edge.pair[0]:
                    vertex.neighbors.append(edge.pair[1])
                    vertex.degree += 1
                elif vertex == edge.pair[1]:
                    vertex.neighbors.append(edge.pair[0])
                    vertex.degree += 1
    
    def has_eulerian_circuit(self):
        for vertex in self.vertices:
            if vertex.degree % 2 != 0:
                return False
        return True
    
    def find_eulerian_circuit(self, vertex):
        for vert in self.vertices:
            if vertex == vert:
                self.circuit.append(vert)
                self.vertices.remove(vert)
                break
        
        for neighbor in vertex.neighbors:
            if neighbor in self.vertices:
                self.find_eulerian_circuit(neighbor)
                break
    
    def circ_to_str(self):
        cric_to_str = ""
        for x in range(0,len(self.circuit)):
            if x < len(self.circuit) - 1:
                cric_to_str += self.circuit[x].label + "-"
            else:
                cric_to_str += self.circuit[x].label
        
        return cric_to_str

    def has_hamiltonian_circuit_dirac(self):
        if len(self.vertices) < 3:
            return False
        else:
            for vertex in self.vertices:
                if vertex.degree < len(self.vertices)/2:
                    return False
            return True
    
    def has_hamiltonian_circuit_ore(self):
        if len(self.vertices) < 3:
            return False
        else:
            for vertex1 in self.vertices:
                for vertex2 in self.vertices:
                    if vertex1 != vertex2:
                        if not vertex2 in vertex1.neighbors:
                            if vertex1.degree + vertex2.degree < len(self.vertices):
                                return False
            return True

class Vertex:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
        self.degree = 0
    
    def __repr__(self):
        return self.label

class Edge:
    def __init__(self, vertex1, vertex2):
        self.pair = (vertex1, vertex2)