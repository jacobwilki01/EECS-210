'''
Name: EECS 210 - Programming Assignment 8 - main.py
Description: This program is a collection of algorithms that solve various graph and game theory problems.

Author: Jacob Wilkus
Date Created: November 14th, 2022

Dependencies: None

Preconditions for Tree(): None
Postconditions for Tree(): 
    - self.root: a Node that is the root of the tree
    - self.height: an integer that is the height of the tree
Pre- and Postconditions for functions in Tree():
    - add_root(): takes in a Vertex() and adds the root to the tree
    - add_child(): takes in a parent Vertex() and a child Vertex() and adds the child to a node in the tree

Preconditions for Vertex():
    - label: a string that is the label of the vertex
Postconditions for Vertex():
    - self.label: a string that is the label of the vertex
    - self.children: a list of Vertices that are the children of the vertex
    - self.level: an integer that is the level of the vertex in the tree
Pre- and Postconditions for functions in Vertex():
    - add_child(): takes in a Vertex() and adds the child to the vertex
'''

#The Tree Class
class Tree:
    def __init__(self):
        #Initialize the tree
        self.root = None
        self.height = 0
    
    #Function to add the root to the tree
    def add_root(self, root):
        self.root = root
    
    #Function to add a child to a vertex in the tree
    def add_child(self, parent, child):
        parent.add_child(child)
        child.level = parent.level + 1
        if child.level > self.height:
            self.height += 1
    
#The Vertex Class
class Vertex:
    def __init__(self, label):
        #Initialize the vertex
        self.label = label
        self.children = []
        self.level = 0
    
    #Function to add a child to the vertex
    def add_child(self, child):
        self.children.append(child)

    #The list representation of the vertex
    def __repr__(self):
        return str(self.label)