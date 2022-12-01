#Programming Assignemnt 8

from graph import Graph

def main():
    graph1 = Graph([('a','b'),('a','d'),('b','c'),('b','d'),('b','e'),('c','f'),('d','e'),('d','g'),('e','f'),('e','h'),('f','h'),('f','i'),('g','h'),('h','i')])

    print("1.)",end=" ")

    if graph1.has_eulerian_circuit():
        print("The graph has the following Euler circuit: " + graph1.find_eulerian_circuit(graph1.vertices[0]))
    else:
        print("The graph does not have an Euler circuit. Here are the vertices with odd degrees:")
        for vertex in graph1.vertices:
            if vertex.degree % 2 != 0:
                print("- Vertex " + vertex.label + " has an odd degree of " + str(vertex.degree))

    graph2 = Graph([('a','b'),('a','c'),('a','e'),('b','c'),('b','e'),('c','d'),('c','e'),('d','e')])
    #graph2 = Graph([('a','b'),('a','c'),('b','c'),('c','f'),('d','e'),('d','f'),('e','f')])

    if graph2.has_hamiltonian_circuit_dirac():
        print("2.) The graph has a Hamilton circuit.")
    else:
        print("2.) The graph does not have a Hamilton circuit.")

if __name__ == '__main__':
    main()