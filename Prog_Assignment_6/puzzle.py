'''
Code Name: EECS 210 - Programming Assignment 6 - puzzle.py
Description: This program contains the classes that are used to solve a sudoku puzzle using a backtracking algorithm.

Author: Jacob Wilkus
Date Created: October 25th, 2022

Preconditions and Postconditions:
    -Puzzle(board)
        -Precondition: imports a list of lists of strings that represent the rows of the puzzle.
        -Postcondition: creates a puzzle object
            -The puzzle object contains a list of lists of cell objects that represent the rows, columns, and blocks of the puzzle.
            -Those rows, columns, and blocks are reprensented by the row, column, and block objects.
        -copy(self)
            -Precondition: None
            -Postcondition: returns a copy of the puzzle object
        -is_solved(self)
            -Precondition: None
            -Postcondition: returns a boolean value that indicates whether or not the puzzle is solved
    -Row(row,index)
        -Precondition: imports a list of cell objects and an integer
        -Postcondition: creates a row object, which contains a list of cell objects and an integer that represents the row's index
    -Column(column,index)
        -Precondition: imports a list of cell objects and an integer
        -Postcondition: creates a column object, which contains a list of cell objects and an integer that represents the column's index
    -Block(block,index)
        -Precondition: imports a list of cell objects and an integer
        -Postcondition: creates a block object, which contains a list of cell objects and an integer that represents the block's index
    -Cell(value,row_index,column_index,block_index)
        -Precondition: imports a string that represents the value, and three integers that represent the cell's row, column, and block indices
        -Postcondition: creates a cell object, which contains a string that represents the value, and three integers that represent the cell's row, column, and block indices
'''

#The code for the Puzzle class
class Puzzle:
    #The constructor for the Puzzle class
    def __init__(self,board):
        self.board = board #The board is the imported list of lists of strings
        
        self.rows = [] #Creates a list to store the row objects
        for i in range(0,len(self.board)): #For each row in the board object
            self.rows.append(Row(self.board[i],i)) #Create a row object and add it to the list of rows
        
        self.columns = [] #Creates a list to store the column objects
        for i in range(0,len(self.rows)): #For each row in the list of rows
            temp = [] #Creates a temporary list to store the cells in the column
            for row in self.rows: #For each row in the list of rows
                temp.append(row.cells[i]) #Add the cell in the column to the temporary list
            self.columns.append(Column(temp,i)) #Create a column object and add it to the list of columns

        self.blocks = [] #Creates a list to store the block objects
        for i in range(0,len(self.rows),3): #For each row in the list of rows, in increments of 3
            for j in range(0,len(self.rows),3): #For each column in the list of columns, in increments of 3
                temp = [] #Creates a temporary list to store the cells in the block
                for row in self.rows[i:i+3]: #For each row in the list of rows, in increments of 3
                    temp.append(row.cells[j:j+3]) #Add the cells in the block to the temporary list
                self.blocks.append(Block(temp)) #Create a block object and add it to the list of blocks

    #The copy method for the Puzzle class
    def copy(self):
        result = [] #Creates a list to store the rows of the copy
        for row in self.rows: #For each row in the list of rows
            temp = [] #Creates a temporary list to store the cells in the row
            for cell in row.cells: #For each cell in the row
                if cell.value == None: #If the cell is empty
                    temp.append("_") #Add an underscore to the temporary list
                else: #If the cell is not empty
                    temp.append(cell.value) #Add the cell's value to the temporary list
            result.append(temp) #Add the temporary list to the list of rows
        return Puzzle(result) #Return a puzzle object with the list of rows

    #The is_solved method for the Puzzle class
    def is_solved(self): 
        for row in self.rows: #For each row in the list of rows
            for cell in row.cells: #For each cell in the row
                if cell.is_empty: #If a cell is empty
                    return False #Return False
        return True #Return True if no cells are empty

    #The __str__ method for the Puzzle class, which is how the puzzle is printed to the console or written to the file
    def __str__(self):
        result = "" #Creates a string to store the puzzle
        for row in self.rows: #For each row in the list of rows
            result += str(row) + "\n" #Add the row to the string
        return result #Return the string

#The code for the Row class
class Row:
    #The constructor for the Row class
    def __init__(self,row,index): 
        self.index = index #The index is the imported integer
        self.cells = [] #Creates a list to store the cell objects
        for cell in row: #For each cell in the row
            self.cells.append(Cell(cell,self.index,0)) #Create a cell object and add it to the list of cells
    
    #The __str__ method for the Row class, which is how the row is printed to the console or written to the file
    def __str__(self):
        result = "" #Creates a string to store the row
        for cell in self.cells: #For each cell in the row
            result += f"{cell} " #Add the cell to the string
        return result #Return the string
    
    #The __repr__ method for the Row class, which is how the row is printed to the console or written to the file while in a list
    def __repr__(self):
        result = "" #Creates a string to store the row
        for cell in self.cells: #For each cell in the row
            result += f"{cell} " #Add the cell to the string
        return result #Return the string

#The code for the Column class
class Column:
    #The constructor for the Column class
    def __init__(self,column,index):
        self.cells = column #The cells are the imported list of cell objects
        self.index = index #The index is the imported integer
        for cell in self.cells: #For each cell in the column
            cell.column_index = self.index #Set the cell's column index to the column's index
    
    #The __str__ method for the Column class, which is how the column is printed to the console or written to the file
    def __str__(self):
        result = "" #Creates a string to store the column
        for cell in self.cells: #For each cell in the column
            result += str(cell) + " " #Add the cell to the string
        return result #Return the string

#The code for the Block class
class Block:
    #The constructor for the Block class
    def __init__(self,block):
        self.cells = [] #Creates a list to store the cell objects
        for row in block: #For each row in the block
            for cell in row: #For each cell in the row
                self.cells.append(cell) #Add the cell to the list of cells
        
        for cell in self.cells: #For each cell in the block
            cell.update_block_index(cell.row_index,cell.column_index) #Update the cell's block index
    #The __str__ method for the Block class, which is how the block is printed to the console or written to the file
    def __str__(self):
        result = "" #Creates a string to store the block
        for cell in self.cells: #For each cell in the block
            result += str(cell) + " " #Add the cell to the string
        return result #Return the string

#The code for the Cell class
class Cell:
    #The constructor for the Cell class
    def __init__(self,value,row_index,column_index):
        self.row_index = row_index #The row index is the imported integer
        self.column_index = column_index #The column index is the imported integer
        
        if value == "_": #If the value is an underscore
            self.is_empty = True #The cell is empty
            self.value = None #The cell's value is None
            self.possible_values = [] #Creates a list to store the possible values
        else: #If the value is not an underscore
            self.is_empty = False #The cell is not empty
            self.value = value #The cell's value is the imported integer
    
    #The update_value method for the Cell class
    def update_value(self,new):
        self.value = new #The cell's value is the imported integer
        self.is_empty = False  #The cell is not empty
    
    #The update_block_index method for the Cell class
    def update_block_index(self,row_index,column_index):
        if row_index in range(0,3): #If the row index is in the first block
            if column_index in range(0,3): #If the column index is in the first block
                self.block_index = 0 #The cell's block index is 0
            elif column_index in range(3,6): #If the column index is in the second block
                self.block_index = 1 #The cell's block index is 1
            elif column_index in range(6,9): #If the column index is in the third block
                self.block_index = 2 #The cell's block index is 2
        elif row_index in range(3,6): #If the row index is in the second block
            if column_index in range(0,3): #If the column index is in the first block
                self.block_index = 3 #The cell's block index is 3
            elif column_index in range(3,6): #If the column index is in the second block
                self.block_index = 4 #The cell's block index is 4
            elif column_index in range(6,9): #If the column index is in the third block
                self.block_index = 5 #The cell's block index is 5
        elif row_index in range(6,9): #If the row index is in the third block
            if column_index in range(0,3): #If the column index is in the first block
                self.block_index = 6 #The cell's block index is 6
            elif column_index in range(3,6): #If the column index is in the second block
                self.block_index = 7 #The cell's block index is 7
            elif column_index in range(6,9): #If the column index is in the third block
                self.block_index = 8 #The cell's block index is 8
    
    #The __str__ method for the Cell class, which is how the cell is printed to the console or written to the file
    def __str__(self):
        if self.is_empty: #If the cell is empty
            return "_" #Return an underscore
        else: #If the cell is not empty
            return str(self.value) #Return the cell's value
    
    #The __repr__ method for the Cell class, which is how the cell is printed to the console or written to the file while in a list
    def __repr__(self):
        if self.is_empty: #If the cell is empty
            return "_" #Return an underscore
        else: #If the cell is not empty
            return str(self.value) #Return the cell's value