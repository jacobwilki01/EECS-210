'''
Name: EECS 210 - Programming Assignment 8
Author: Jacob Wilkus
'''

from graph import Graph
from nim import NimGame

def main():
    letters = ['a', 'b']

    graphs1 = [
        Graph([('a','b'),('a','e'),('b','e'),('c','d'),('c','e'),('d','e')], "G1"),
        Graph([('a','b'),('a','d'),('a','e'),('b','c'),('b','e'),('c','d'),('c','e'),('d','e')], "G2"),
        Graph([('a','b'),('a','c'),('a','d'),('b','d'),('b','e'),('c','d'),('d','e')], "G3"),
        Graph([('a','b'),('a','c'),('a','d'),('b','a'),('b','d'),('c','a'),('c','d')],"Bridges of Königsberg"),
        Graph([('a','b'),('a','d'),('b','c'),('b','d'),('b','e'),('c','f'),('d','e'),('d','g'),('e','f'),('e','h'),('f','h'),('f','i'),('g','h'),('h','i')], "Test Graph #1")
    ]
    
    for x in range(0,len(graphs1)):
        print(f"1{letters[x // 4]}.) ",end="")
        if graphs1[x].has_eulerian_circuit():
            graphs1[x].find_eulerian_circuit(graphs1[x].vertices[0])
            print(f"The graph, {graphs1[x].name}, has the following Euler circuit: " + graphs1[x].circ_to_str())
        else:
            print(f"The graph, {graphs1[x].name}, does not have an Euler circuit. Here are the vertices with odd degrees:")
            for vertex in graphs1[x].vertices:
                if vertex.degree % 2 != 0:
                    print("- Vertex " + vertex.label + " has an odd degree of " + str(vertex.degree))
    
    print("")

    graphs2 = [
        Graph([('a','b'),('a','c'),('a','e'),('b','c'),('b','e'),('c','d'),('c','e'),('d','e')], "G1"),
        Graph([('a','b'),('b','c'),('b','d'),('c','d')], "G2"),
        Graph([('a','b'),('b','c'),('b','g'),('c','d'),('c','e'),('e','f'),('e','g')], "G3"),
        Graph([('a','b'),('a','c'),('a','e'),('b','c'),('b','e'),('c','d'),('c','e'),('d','e')], "Test Graph #2")
    ]
    
    for x in range(0,len(graphs2)):
        print(f"2{letters[x // 3]}.) ",end="")
        if graphs2[x].has_hamiltonian_circuit_dirac():
            print(f"The graph, {graphs2[x].name}, has a Hamilton circuit according to Dirac's Theorem.")
        else:
            print(f"The graph, {graphs2[x].name}, does not have a Hamilton circuit according to Dirac's Theorem.")
    
    print("")

    for x in range(0,len(graphs2)):
        print(f"3{letters[x // 3]}.) ",end="")
        if graphs2[x].has_hamiltonian_circuit_ore():
            print(f"The graph, {graphs2[x].name}, has a Hamilton circuit according to Ore's Theorem.")
        else:
            print(f"The graph, {graphs2[x].name}, does not have a Hamilton circuit according to Ore's Theorem.")
    
    print("")

    games4 = [
        NimGame((2,2,1),"Debug Game"),
        NimGame((1,2,3),"Test Game")
    ]

    for x in range(0,len(games4)):
        print(f"4{letters[x]}.) ",end="")
        if games4[x].tree.root.value == 1:
            print(f"For the {games4[x].name} Player 1 is the winner.")
        else:
            print(f"For the {games4[x].name} Player 2 is the winner.")
        
        

if __name__ == '__main__':
    main()