'''
Code Name: EECS 210 - Programming Assignment 6 - main.py
Description: This program solves a sudoku puzzle using a backtracking algorithm.

Author: Jacob Wilkus
Date Created: October 25th, 2022

Dependencies: puzzle.py

Preconditions and Postconditions:
    -main()
        -Precondition: None
        -Postcondition: The program will run and solve the puzzles in the files puzzle1.txt, puzzle2.txt, puzzle3.txt, puzzle4.txt, and puzzle5.txt. 
        -The solutions will be written to the files solution1.txt, solution2.txt, solution3.txt, solution4.txt, and solution5.txt.
        -The program will also print the solutions to the console.
    -puzzle_to_list(file)
        -Precondition: imports a file with a sudoku puzzle
        -Postcondition: returns a list of lists of strings that represent the rows of the puzzle.
    -solution_to_file(solution,output)
        -Precondition: imports a solution to a puzzle and a file name
        -Postcondition: writes the solution to the file
    -add_message(solution,output)
        -Precondition: imports a solution to a puzzle and a file name
        -Postcondition: writes a message to the file that indicates whether or not a solution was found. If no solution was found, it will also indicate which cell has no possible values.
    -create_puzzle(file)
        -Precondition: imports a file with a sudoku puzzle
        -Postcondition: returns a puzzle object
    -solve_puzzle(puzzle)
        -Precondition: imports a puzzle object
        -Postcondition: returns a list with a boolean value that indicates whether or not a solution was found and the puzzle object
        -This function uses a backtracking algorithm to solve the puzzle, recursively calling it self until a solution is found.
    -find_possible_values(cell,puzzle)
        -Precondition: imports a cell object and a puzzle object
        -Postcondition: returns a list of integers that are possible values for the cell
    -is_valid(value,cell,puzzle)
        -Precondition: imports an integer, a cell object, and a puzzle object
        -Postcondition: returns a boolean value that indicates whether or not the value is valid for the cell
    -is_valid_in_row(value,cell,puzzle)
        -Precondition: imports an integer, a cell object, and a puzzle object
        -Postcondition: returns a boolean value that indicates whether or not the value is valid for the cell's row
    -is_valid_in_column(value,cell,puzzle)
        -Precondition: imports an integer, a cell object, and a puzzle object
        -Postcondition: returns a boolean value that indicates whether or not the value is valid for the cell's column
    -is_valid_in_block(value,cell,puzzle)
        -Precondition: imports an integer, a cell object, and a puzzle object
        -Postcondition: returns a boolean value that indicates whether or not the value is valid for the cell's block
            -The block is the 3x3 square that the cell is in
'''

from puzzle import * #Imports puzzle.py

#The main() function for the program
def main():
    files = ["puzzle1.txt","puzzle2.txt","puzzle3.txt","puzzle4.txt","puzzle5.txt"] #The names of the files that contain the puzzles
    for x in range(0,len(files)): #iterates through the files
        print(f"\nProcessing {files[x]}") #prints the name of the file that is being processed
        puzzle = create_puzzle(files[x]) #creates a puzzle object from the file
        solution = solve_puzzle(puzzle) #initial call of solve_puzzle()
        if not solution[0]: #if no solution was found
            print("No solution found!") #prints a message to the console
        for row in solution[1].rows: #iterates through the rows of the puzzle
            for cell in row.cells: #iterates through the cells of the row
                print("_" if cell.is_empty else cell.value, end=" ") #prints the value of the cell or an underscore if the cell is empty
            print() #prints a new line
        for row in solution[1].rows: #iterates through the rows of the puzzle
            for cell in row.cells: #iterates through the cells of the row
                if cell.is_empty: #if the cell is empty
                    #prints a message to the console that indicates which cell has no possible values
                    print("No solution found because the cell at row " + str(cell.row_index + 1) + ", column " + str(cell.column_index + 1) + " has no possible values.")
                    break #breaks out of the loop
            if cell.is_empty: #if the cell is empty
                break #breaks out of the loop
        solution_to_file(solution[1],f"solution{x + 1}.txt") #writes the solution to the file
        add_message(solution,f"solution{x + 1}.txt") #writes a message to the file that indicates whether or not a solution was found

#Code for puzzle_to_list()
def puzzle_to_list(file):
    result = [] #The list that will be returned
    temp = [] #A temporary list that will be used to store the rows of the puzzle

    for line in file: #iterates through the lines of the file
        temp.append(line.strip()) #adds the line to the temporary list
    
    for row in temp: #iterates through the rows of the puzzle
        result.append(row.split()) #adds the row to the result list

    return result #returns the result list

#Code for solution_to_file()
def solution_to_file(solution,output):
    file = open(output,"w") #opens the file
    for row in solution.rows: #iterates through the rows of the puzzle
        for cell in row.cells: #iterates through the cells of the row
            file.write("_" if cell.is_empty else cell.value) #writes the value of the cell or an underscore if the cell is empty
            file.write(" ") #writes a space
        file.write("\n") #writes a new line
    file.close() #closes the file

#Code for add_message()
def add_message(solution,output):
    print(f"Answer written to {output}\n") #prints a message to the console
    file = open(output,"a") #opens the file
    file.write("\n") #writes a new line
    if solution[0]: #if a solution was found
        file.write("Solution found!") #writes a message to the file
    else: #if no solution was found
        for row in solution[1].rows: #iterates through the rows of the puzzle
            for cell in row.cells: #iterates through the cells of the row
                if cell.is_empty: #if the cell is empty
                    #writes a message to the file that indicates which cell has no possible values
                    file.write("No solution found because the cell at row " + str(cell.row_index + 1) + ", column " + str(cell.column_index + 1) + " has no possible values.")
                    break #breaks out of the loop
            if cell.is_empty: #if the cell is empty
                break #breaks out of the loop
    file.close() #closes the file

#Code for create_puzzle()
def create_puzzle(file): 
    file = open(file, "r") #opens the file
    puzzle = Puzzle(puzzle_to_list(file)) #creates a puzzle object from the file
    file.close() #closes the file
    return puzzle #returns the puzzle object

#Code for solve_puzzle()
def solve_puzzle(puzzle): 
    to_solve = [] #A list that will be used to store the cells that need to be solved
    for row in puzzle.rows: #iterates through the rows of the puzzle
        for cell in row.cells: #iterates through the cells of the row
            if cell.is_empty: #if the cell is empty
                to_solve.append(cell) #adds the cell to the list of cells that need to be solved

    if puzzle.is_solved(): #if the puzzle is solved
        print("Solution found!") #prints a message to the console
        return [True, puzzle] #returns a list that contains a boolean value that indicates whether or not a solution was found and the puzzle object

    to_solve[0].possible_values = find_possible_values(to_solve[0],puzzle) #finds the possible values for the first cell in the list of cells that need to be solved
    if len(to_solve[0].possible_values) == 0: #if the cell has no possible values
        return [False, puzzle] #returns a list that contains a boolean value that indicates that no solution was found and the puzzle object
    elif len(to_solve[0].possible_values) == 1: #if the cell has only one possible value
        new = puzzle.copy() #creates a copy of the puzzle object
        new.rows[to_solve[0].row_index].cells[to_solve[0].column_index].update_value(str(to_solve[0].possible_values[0])) #updates the value of the cell in the copy of the puzzle object
        new.rows[to_solve[0].row_index].cells[to_solve[0].column_index].is_empty = False #updates the is_empty attribute of the cell in the copy of the puzzle object
        move = solve_puzzle(new) #recursive call of solve_puzzle()
        if move[0]: #if a solution was found
            return move #returns the list that contains a boolean value that indicates that a solution was found and the puzzle object
    else: #if the cell has more than one possible value
        for i in range(len(to_solve[0].possible_values)): #iterates through the possible values of the cell
            new = puzzle.copy() #creates a copy of the puzzle object
            new.rows[to_solve[0].row_index].cells[to_solve[0].column_index].update_value(str(to_solve[0].possible_values[i])) #updates the value of the cell in the copy of the puzzle object
            new.rows[to_solve[0].row_index].cells[to_solve[0].column_index].is_empty = False #updates the is_empty attribute of the cell in the copy of the puzzle object
            move = solve_puzzle(new) #recursive call of solve_puzzle()
            if move[0]: #if a solution was found
                break #breaks out of the loop
    
    return move #returns the list that contains a boolean value that indicates whether or not a solution was found and the puzzle object

#Code for find_possible_values()
def find_possible_values(cell,puzzle):
    possible_values = [] #A list that will be used to store the possible values of the cell
    for i in range(1,10): #iterates through the numbers 1 to 9
        if is_valid(i,cell,puzzle): #if the number is valid using is_valid()
            possible_values.append(i) #adds the number to the list of possible values
    return possible_values #returns the list of possible values

#Code for is_valid()
def is_valid(value,cell,puzzle):
    #checks if the value is valid in the row, column, and box of the cell
    if is_valid_in_row(value,cell,puzzle) and is_valid_in_column(value,cell,puzzle) and is_valid_in_block(value,cell,puzzle):
        return True #returns True if the value is valid
    return False #returns False if the value is not valid

#Code for is_valid_in_row()
def is_valid_in_row(value,cell,puzzle):
    for cell in puzzle.rows[cell.row_index].cells: #iterates through the cells of the row
        if cell.value == str(value): #if the value is already in the row
            return False #returns False
    return True #returns True if the value is not in the row

#Code for is_valid_in_column()
def is_valid_in_column(value,cell,puzzle): 
    for cell in puzzle.columns[cell.column_index].cells: #iterates through the cells of the column
        if cell.value == str(value): #if the value is already in the column
            return False #returns False
    return True #returns True if the value is not in the column

def is_valid_in_block(value,cell,puzzle):
    for cell in puzzle.blocks[cell.block_index].cells: #iterates through the cells of the box
        if cell.value == str(value): #if the value is already in the box
            return False #returns False
    return True #returns True if the value is not in the box

#Python method for calling the main() function
if __name__ == "__main__":
    main()