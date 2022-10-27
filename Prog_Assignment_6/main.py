from puzzle import *

def main():
    files = ["puzzle1.txt","puzzle2.txt","puzzle3.txt","puzzle4.txt","puzzle5.txt"]
    for x in range(0,len(files)):
        print(f"Processing {files[x]}")
        puzzle = create_puzzle(files[x])
        solution = solve_puzzle(puzzle)
        if not solution[0]:
            print("No solution found!")
        solution_to_file(solution[1],f"solution{x + 1}.txt")
        add_message(solution,f"solution{x + 1}.txt")

def puzzle_to_list(file):
    result = []
    temp = []

    for line in file:
        temp.append(line.strip())
    
    for row in temp:
        result.append(row.split())

    return result

def solution_to_file(solution,output):
    file = open(output,"w")
    for row in solution.rows:
        for cell in row.cells:
            file.write("_" if cell.is_empty else cell.value)
            file.write(" ")
        file.write("\n")
    file.close()

def add_message(solution,output):
    print(f"Answer written to {output}\n")
    file = open(output,"a")
    file.write("\n")
    if solution[0]:
        file.write("Solution found!")
    else:
        for row in solution[1].rows:
            for cell in row.cells:
                if cell.is_empty:
                    file.write("No solution found because the cell at row " + str(cell.row_index + 1) + ", column " + str(cell.column_index + 1) + " has no possible values.")
                    break
            if cell.is_empty:
                break
    file.close()

def create_puzzle(file):
    file = open(file, "r")
    puzzle = Puzzle(puzzle_to_list(file))
    file.close()
    return puzzle

def solve_puzzle(puzzle):
    to_solve = []
    for row in puzzle.rows:
        for cell in row.cells:
            if cell.is_empty:
                to_solve.append(cell)

    if puzzle.is_solved():
        print("Solution found!")
        return [True, puzzle]

    to_solve[0].possible_values = find_possible_values(to_solve[0],puzzle)
    if len(to_solve[0].possible_values) == 0:
        return [False, puzzle]
    elif len(to_solve[0].possible_values) == 1:
        new = puzzle.copy()
        new.rows[to_solve[0].row_index].cells[to_solve[0].column_index].update_value(str(to_solve[0].possible_values[0]))
        new.rows[to_solve[0].row_index].cells[to_solve[0].column_index].is_empty = False
        move = solve_puzzle(new)
        if move[0]:
            return move
    else:
        for i in range(len(to_solve[0].possible_values)):
            new = puzzle.copy()
            new.rows[to_solve[0].row_index].cells[to_solve[0].column_index].update_value(str(to_solve[0].possible_values[i]))
            new.rows[to_solve[0].row_index].cells[to_solve[0].column_index].is_empty = False
            move = solve_puzzle(new)
            if move[0]:
                break
    
    return move

def find_possible_values(cell,puzzle):
    possible_values = []
    for i in range(1,10):
        if is_valid(i,cell,puzzle):
            possible_values.append(i)
    return possible_values

def is_valid(value,cell,puzzle):
    if is_valid_in_row(value,cell,puzzle) and is_valid_in_column(value,cell,puzzle) and is_valid_in_block(value,cell,puzzle):
        return True
    return False

def is_valid_in_row(value,cell,puzzle):
    for cell in puzzle.rows[cell.row_index].cells:
        if cell.value == str(value):
            return False
    return True

def is_valid_in_column(value,cell,puzzle):
    for cell in puzzle.columns[cell.column_index].cells:
        if cell.value == str(value):
            return False
    return True

def is_valid_in_block(value,cell,puzzle):
    for cell in puzzle.blocks[cell.block_index].cells:
        if cell.value == str(value):
            return False
    return True

if __name__ == "__main__":
    main()