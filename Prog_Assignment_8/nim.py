'''
Name: EECS 210 - Programming Assignment 8 - main.py
Description: This program is a collection of algorithms that solve various graph and game theory problems.

Author: Jacob Wilkus
Date Created: November 14th, 2022

Dependencies: tree.py

Preconditions for NimGame():
    - piles: a tuple of integers that are the number of stones in each pile
    - name: a string that is the name of the game
Postconditions for NimGame():
    - self.piles: a tuple of integers that are the number of stones in each pile
    - self.name: a string that is the name of the game
    - self.tree: a MinMaxTree() that is the game tree of the game
Pre- and Postconditions for functions in NimGame():
    - play(): Calls the play_rec() function on the root of the game tree; Then calls det_values() to determine the values of the nodes in the game tree
    - play_rec(): Takes in a Vertex() and recursively adds the children of the vertex to the game tree for every possible move until the game is over
    - det_values(): Recursively determines the values (-1 or 1) of the nodes in the game tree

Preconditions for MinMaxTree(): 
    - Inherits from Tree()
Postconditions for MinMaxTree(): 
    - Inherits from Tree()
    - self.levels: a list of lists of Vertices that are the vertices in each level of the tree
Pre- and Postconditions for functions in MinMaxTree():
    - add_root(): Inherits from Tree() and adds the root level to self.levels
    - add_child(): Inherits from Tree() and adds the child it's level in self.levels

Preconditions for NimVertex():
    - Inherits from Vertex()
Postconditions for NimVertex():
    - Inherits from Vertex()
    - self.value: an integer that is the value of the vertex
Pre- and Postconditions for functions in NimVertex():
    - update(): Takes in an integer and updates the value of the vertex
'''

from tree import Tree, Vertex

#The NimGame Class
class NimGame:
    def __init__(self,piles,name=""):
        #Initialize the game
        self.tree = MinMaxTree()
        self.tree.add_root(NimVertex(piles))
        self.name = name
        self.play()
    
    def play(self):
        #Play the game by calling the recursive function
        self.play_rec(self.tree.root)
        #Determine the values of the vertexes in the tree
        self.det_values()
    
    def play_rec(self,vertex):
        #If the game is over, return
        if vertex.label[0] == 0 and vertex.label[1] == 0 and vertex.label[2] == 0:
            if vertex.level % 2 == 0:
                vertex.update(1) #Player 2 wins
            else:
                vertex.update(-1) #Player 1 wins
            return
        else:
            for i in range(0,3): #For each pile
                for j in range(1,vertex.label[i]+1): #For each stone in the pile
                    new_piles = list(vertex.label) #Make a copy of the piles
                    new_piles[i] -= j #Remove the stones 
                    new_piles = tuple(new_piles) #Make it a tuple 
                    new_vertex = NimVertex(new_piles) #Make a new vertex 
                    self.tree.add_child(vertex,new_vertex) #Add the vertex to the tree
                    self.play_rec(new_vertex) #Recursively call the function
    
    #Function to determine the values of the vertexes in the tree
    def det_values(self):
        for x in range(len(self.tree.levels)-2, -1, -1): #For each level in the tree
            for vertex in self.tree.levels[x]: #For each vertex in the level
                if len(vertex.children) > 0: #If the vertex has children
                    if vertex.level % 2 == 0: #If it's player 1's turn
                        vertex.value = max([child.value for child in vertex.children]) #Set the value to the max of the children
                    else: #If it's player 2's turn
                        vertex.value = min([child.value for child in vertex.children]) #Set the value to the min of the children

#The NimVertex Class
class NimVertex(Vertex):
    def __init__(self, label):
        super().__init__(label) #Initialize the vertex from Vertex()
        self.value = 0 #Initialize the value to 0
    
    #Function to update the value of the vertex
    def update(self,value): 
        self.value = value

#The MinMaxTree Class
class MinMaxTree(Tree):
    def __init__(self):
        super().__init__() #Initialize the tree from Tree()
        self.levels = [] #Initialize the levels to an empty list
    
    #Function to add the root to the tree
    def add_root(self, root):
        super().add_root(root) #Add the root from Tree()
        self.levels.append([root]) #Add the root to the levels
    
    #Function to add a child to the tree
    def add_child(self, parent, child):
        super().add_child(parent,child) #Add the child from Tree()
        if child.level == len(self.levels): #If the child is in a new level
            self.levels.append([child]) #Add the child to levels in a new level
        else:
            self.levels[child.level].append(child) #Add the child to the pre-made level