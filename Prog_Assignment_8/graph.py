'''
Name: EECS 210 - Programming Assignment 8 - main.py
Description: This program is a collection of algorithms that solve various graph and game theory problems.

Author: Jacob Wilkus
Date Created: November 14th, 2022

Dependencies: None

Preconditions for Graph():
    - edges: a list of tuples of vertices that are connected by an edge
    - name: a string that is the name of the graph
Postconditions for Graph():
    - self.edges: a list of tuples of vertices that are connected by an edge
    - self.vertices: a list of vertices that are in the graph
    - self.name: a string that is the name of the graph
    - self.circuit: a list of vertices that is the Euler circuit of the graph
Pre- and Postconditions for functions in Graph():
    - has_eulerian_circuit(): returns True if the graph has an Euler circuit, False otherwise
    - find_eulerian_circuit(): finds the Euler circuit of the graph
    - has_hamiltonian_circuit_dirac(): returns True if the graph has a Hamilton circuit according to Dirac's Theorem, False otherwise
    - has_hamiltonian_circuit_ore(): returns True if the graph has a Hamilton circuit according to Ore's Theorem, False otherwise
    - circ_to_str(): returns a string of the vertices in the Euler circuit

Preconditions for Vertex():
    - label: a string that is the label of the vertex
Postconditions for Vertex():
    - self.label: a string that is the label of the vertex
    - self.degree: an integer that is the degree of the vertex
    - self.edges: a list of tuples of vertices that are connected by an edge
'''

#the Graph class
class Graph:
    def __init__(self, edges, name=""): #constructor
        #General graph properties as instance variables
        self.vertices = []
        self.edges = []
        self.circuit = []
        self.name = name

        #Append every instance of a vertex to self.vertices
        for edge in edges:
            self.vertices.append(edge[0])
            self.vertices.append(edge[1])
        
        #Remove duplicates from self.vertices and sort it.
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        #Turn every vertex in self.vertices into a Vertex object
        for x in range(0,len(self.vertices)):
            self.vertices[x] = Vertex(self.vertices[x])

        #Append every edge to self.edges
        for edge in edges:
            self.edges.append(Edge(edge[0], edge[1]))
        
        #For every edge in self.edges, make sure the values are refering to the Vertex objects in self.vertices
        for edge in self.edges: #iterates over every edge in self.edges
            for vertex in self.vertices: #iterates over every vertex in self.vertices
                if edge.pair[0] == vertex.label: #if the first value in the edge is the same as the label of the vertex
                    edge.pair = (vertex, edge.pair[1]) #replace the first value in the edge with the vertex object
                elif edge.pair[1] == vertex.label: #if the second value in the edge is the same as the label of the vertex
                    edge.pair = (edge.pair[0], vertex) #replace the second value in the edge with the vertex object

        #Based on every edge, make sure each respective vertex has the correct degree and neighbors
        for vertex in self.vertices: #iterates over every vertex in self.vertices
            for edge in self.edges: #iterates over every edge in self.edges
                if vertex == edge.pair[0]: #if the vertex is the first value in the edge
                    vertex.neighbors.append(edge.pair[1]) #add the second value in the edge to the vertex's neighbors
                    vertex.degree += 1 #increase the vertex's degree by 1
                elif vertex == edge.pair[1]: #if the vertex is the second value in the edge
                    vertex.neighbors.append(edge.pair[0]) #add the first value in the edge to the vertex's neighbors
                    vertex.degree += 1 #increase the vertex's degree by 1
    
    #Function for determining if the graph has an Euler circuit
    def has_eulerian_circuit(self):
        for vertex in self.vertices: #iterates over every vertex in self.vertices
            if vertex.degree % 2 != 0: #if the degree of the vertex is not even
                return False #return False
        return True #else, return True
    
    #Function for finding the Euler circuit of the graph
    def find_eulerian_circuit(self, vertex):
        for vert in self.vertices: #iterates over every vertex in self.vertices
            if vertex == vert: #if the vertex is the same as the vertex in self.vertices
                self.circuit.append(vert) #add the vertex to the Euler circuit
                self.vertices.remove(vert) #remove the vertex from self.vertices
                break #break out of the loop
        
        for neighbor in vertex.neighbors: #iterates over every neighbor of the vertex
            if neighbor in self.vertices: #if the neighbor is in self.vertices
                self.find_eulerian_circuit(neighbor) #call the function again with the neighbor as the vertex
                break #break out of the loop
    
    #Function for converting the Euler circuit to a string
    def circ_to_str(self):
        cric_to_str = "" #create an empty string
        for x in range(0,len(self.circuit)): #iterates over every vertex in the Euler circuit
            if x < len(self.circuit) - 1: #if the index is less than the length of the Euler circuit - 1
                cric_to_str += self.circuit[x].label + "-" #add the label of the vertex and a dash to the string
            else:
                cric_to_str += self.circuit[x].label #add the label of the vertex to the string
        
        return cric_to_str #return the string

    #Function for determining if the graph has a Hamilton circuit according to Dirac's Theorem
    def has_hamiltonian_circuit_dirac(self):
        if len(self.vertices) < 3: #if the number of vertices is less than 3 return False
            return False 
        else: 
            for vertex in self.vertices: #iterates over every vertex in self.vertices
                if vertex.degree < len(self.vertices)/2: #if the degree of the vertex is less than the number of vertices divided by 2, return False
                    return False
            return True #else, return True
    
    #Function for determining if the graph has a Hamilton circuit according to Ore's Theorem
    def has_hamiltonian_circuit_ore(self):
        if len(self.vertices) < 3: #if the number of vertices is less than 3 return False
            return False
        else:
            for vertex1 in self.vertices: #iterates over every vertex in self.vertices
                for vertex2 in self.vertices: #iterates over every vertex in self.vertices again
                    if vertex1 != vertex2: #if the two vertices are not the same
                        if not vertex2 in vertex1.neighbors: #if the second vertex is not in the first vertex's neighbors
                            if vertex1.degree + vertex2.degree < len(self.vertices): #if the sum of the degrees of the two vertices is less than the number of vertices, return False
                                return False
            return True #else, return True

#the Vertex class
class Vertex:
    def __init__(self, label):
        #General vertex properties as instance variables
        self.label = label
        self.neighbors = []
        self.degree = 0
    
    #The list representation of the vertex
    def __repr__(self):
        return self.label

#the Edge class
class Edge:
    def __init__(self, vertex1, vertex2):
        self.pair = (vertex1, vertex2) #the pair of vertices that the edge connects