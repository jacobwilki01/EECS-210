class Puzzle:
    def __init__(self,board):
        self.board = board
        
        self.rows = []
        for i in range(0,len(self.board)):
            self.rows.append(Row(self.board[i],i))
        
        self.columns = []
        for i in range(0,len(self.rows)):
            temp = []
            for row in self.rows:
                temp.append(row.cells[i])
            self.columns.append(Column(temp,i))

        self.blocks = []
        for i in range(0,len(self.rows),3):
            for j in range(0,len(self.rows),3):
                temp = []
                for row in self.rows[i:i+3]:
                    temp.append(row.cells[j:j+3])
                self.blocks.append(Block(temp))
    def copy(self):
        result = []
        for row in self.rows:
            temp = []
            for cell in row.cells:
                if cell.value == None:
                    temp.append("_")
                else:
                    temp.append(cell.value)
            result.append(temp)
        return Puzzle(result)
    def is_solved(self):
        for row in self.rows:
            for cell in row.cells:
                if cell.is_empty:
                    return False
        return True
    def __str__(self):
        result = ""
        for row in self.rows:
            result += str(row) + "\n"
        return result

class Row:
    def __init__(self,row,index):
        self.row = row
        self.index = index
        self.cells = []
        for cell in row:
            self.cells.append(Cell(cell,self.index,0))
    def __str__(self):
        result = ""
        for cell in self.cells:
            result += f"{cell} "
        return result
    def __repr__(self):
        result = ""
        for cell in self.cells:
            result += f"{cell} "
        return result

class Column:
    def __init__(self,column,index):
        self.cells = column
        self.index = index
        for cell in self.cells:
            cell.column_index = self.index
    def __str__(self):
        result = ""
        for cell in self.cells:
            result += str(cell) + " "
        return result

class Block:
    def __init__(self,block):
        self.cells = []
        for row in block:
            for cell in row:
                self.cells.append(cell)
        
        for cell in self.cells:
            cell.update_block_index(cell.row_index,cell.column_index)
    def __str__(self):
        result = ""
        for cell in self.cells:
            result += str(cell) + " "
        return result

class Cell:
    def __init__(self,value,row_index,column_index):
        self.row_index = row_index
        self.column_index = column_index

        if value == "_":
            self.is_empty = True
            self.value = None
            self.possible_values = []
        else:
            self.is_empty = False
            self.value = value
    def update_value(self,new):
        self.value = new
        self.is_empty = False
    def update_block_index(self,row_index,column_index):
        if row_index in range(0,3):
            if column_index in range(0,3):
                self.block_index = 0
            elif column_index in range(3,6):
                self.block_index = 1
            elif column_index in range(6,9):
                self.block_index = 2
        elif row_index in range(3,6):
            if column_index in range(0,3):
                self.block_index = 3
            elif column_index in range(3,6):
                self.block_index = 4
            elif column_index in range(6,9):
                self.block_index = 5
        elif row_index in range(6,9):
            if column_index in range(0,3):
                self.block_index = 6
            elif column_index in range(3,6):
                self.block_index = 7
            elif column_index in range(6,9):
                self.block_index = 8
    def __str__(self):
        if self.is_empty:
            return "_"
        else:
            return str(self.value)
    def __repr__(self):
        if self.is_empty:
            return "_"
        else:
            return str(self.value)