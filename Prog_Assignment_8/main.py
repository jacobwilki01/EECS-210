'''
Name: EECS 210 - Programming Assignment 8 - main.py
Description: This program is a collection of algorithms that solve various graph and game theory problems.

Author: Jacob Wilkus
Date Created: November 14th, 2022

Dependencies: graph.py, nim.py

Preconditions for main(): None
Postconditions for main(): Prints the relevant outputs for each problem.
'''

#Imports the Graph class and NimGame class from their respective files.
from graph import Graph
from nim import NimGame

#The main function that calls the functions to solve the problems.
def main():
    letters = ['a', 'b'] #The letters that will be used to label the the answers to the problems.

    #Graphs for the first problem.
    graphs1 = [
        Graph([('a','b'),('a','e'),('b','e'),('c','d'),('c','e'),('d','e')], "G1"),
        Graph([('a','b'),('a','d'),('a','e'),('b','c'),('b','e'),('c','d'),('c','e'),('d','e')], "G2"),
        Graph([('a','b'),('a','c'),('a','d'),('b','d'),('b','e'),('c','d'),('d','e')], "G3"),
        Graph([('a','b'),('a','c'),('a','d'),('b','a'),('b','d'),('c','a'),('c','d')],"Bridges of Königsberg"),
        Graph([('a','b'),('a','d'),('b','c'),('b','d'),('b','e'),('c','f'),('d','e'),('d','g'),('e','f'),('e','h'),('f','h'),('f','i'),('g','h'),('h','i')], "Test Graph #1")
    ]
    
    #Iterates through the graphs and prints the answers to the first problem.
    for x in range(0,len(graphs1)):
        print(f"1{letters[x // 4]}.) ",end="") #Prints the question number.
        if graphs1[x].has_eulerian_circuit(): #If the graph has an Euler circuit, print the circuit.
            graphs1[x].find_eulerian_circuit(graphs1[x].vertices[0]) #Finds the Euler circuit.
            print(f"The graph, {graphs1[x].name}, has the following Euler circuit: " + graphs1[x].circ_to_str()) #Prints the Euler circuit.
        else: #If the graph does not have an Euler circuit, print that it does not have an Euler circuit.
            print(f"The graph, {graphs1[x].name}, does not have an Euler circuit. Here are the vertices with odd degrees:")
            for vertex in graphs1[x].vertices: #Iterates through the vertices and prints the vertices with odd degrees.
                if vertex.degree % 2 != 0: #If the vertex has an odd degree, print it.
                    print("- Vertex " + vertex.label + " has an odd degree of " + str(vertex.degree))
    
    print("") #Prints a blank line for spacing.

    #Graphs for the second problem.
    graphs2 = [
        Graph([('a','b'),('a','c'),('a','e'),('b','c'),('b','e'),('c','d'),('c','e'),('d','e')], "G1"),
        Graph([('a','b'),('b','c'),('b','d'),('c','d')], "G2"),
        Graph([('a','b'),('b','c'),('b','g'),('c','d'),('c','e'),('e','f'),('e','g')], "G3"),
        Graph([('a','b'),('a','c'),('a','e'),('b','c'),('b','e'),('c','d'),('c','e'),('d','e')], "Test Graph #2")
    ]
    
    #Iterates through the graphs and prints the answers to the second problem.
    for x in range(0,len(graphs2)):
        print(f"2{letters[x // 3]}.) ",end="") #Prints the question number.
        if graphs2[x].has_hamiltonian_circuit_dirac(): #If the graph has a Hamilton circuit, print the circuit.
            print(f"The graph, {graphs2[x].name}, has a Hamilton circuit according to Dirac's Theorem.")
        else: #If the graph does not have a Hamilton circuit, print that it does not have a Hamilton circuit.
            print(f"The graph, {graphs2[x].name}, does not have a Hamilton circuit according to Dirac's Theorem.")
    
    print("") #Prints a blank line for spacing.

    #iterates through the graphs and prints the answers to the third problem.
    for x in range(0,len(graphs2)):
        print(f"3{letters[x // 3]}.) ",end="") #Prints the question number.
        if graphs2[x].has_hamiltonian_circuit_ore(): #If the graph has a Hamilton circuit, print the circuit.
            print(f"The graph, {graphs2[x].name}, has a Hamilton circuit according to Ore's Theorem.")
        else: #If the graph does not have a Hamilton circuit, print that it does not have a Hamilton circuit.
            print(f"The graph, {graphs2[x].name}, does not have a Hamilton circuit according to Ore's Theorem.")
    
    print("") #Prints a blank line for spacing.

    #Games for the fourth problem.
    games4 = [
        NimGame((2,2,1),"Debug Game"),
        NimGame((1,2,3),"Test Game")
    ]

    #Iterates through the games and prints the answers to the fourth problem.
    for x in range(0,len(games4)):
        print(f"4{letters[x]}.) ",end="") #Prints the question number.
        if games4[x].tree.root.value == 1: #If the winner is Player 1, print that Player 1 wins.
            print(f"For the {games4[x].name} Player 1 (1) is the winner.")
        else: #If the winner is Player 2, print that Player 2 wins.
            print(f"For the {games4[x].name} Player 2 (-1) is the winner.")
        
#Calls the main function.
if __name__ == '__main__':
    main()