for x in range(0,len(results)): #iterates over results
        if x == 0:
            print(results[x]) #prints the name of the function first, only at index 0.
        else:
            for item in results[x]: #fixes the formatting, as described below!
                if item != True and item != False:
                    pass #skips for index 0, becasue it is just the name!
                else: #turns the boolean values of True and False into strings more easily usable for printing the table.
                    if item == True:
                        item = "T"
                    else:
                        item = "F"
            if x == 1: #when it is index 1, it creates the rows rather than adding to them like for the other indexes
                rows = [] #list of each row to print
                rows.append(f"| {results[x][0]} |") #creates row 1, the identifier row that handles the name of each column. appends it to rows.
                
                rows.append("|---|") #creates row 2, the line in between the identifier and values. appends it to rows.
                
                #creates rows 3-6 by simply calling each respective value.
                for y in range(1,5): #iterates over 1-4
                    rows.append(f"| {results[x][y]} |")

                if len(results[x]) == 9: #9 is the size if there are three variables. simply adds the extra rows if applicable
                    #creates the extra rows 7-10, if applicable
                    for y in range(6,10): #iterates over 6-9
                        rows.append(f"| {results[x][y]} |")
            else: #adds to the rows previously made for index 1!
                rows[0] += f" {results[x][0]} |" #adds the next column to the identifier row

                for _ in range(0,len(results[x][0])): #adds to row 2 the necessary amount of space, dependent on how many characters are in the identifier row.
                    rows[1] += "-"
                rows[1] += "--|" #adds the parts of this row that inevitably need to be added to account for the always present blank space!

                blank_space = "" #creates a blank_space string that we will concatenate to each following row on either side of the column's value
                for _ in range(0,len(results[x][0]) % 2): #iterates over half of the length of the identifier and creates the relevant amount of blank space for blank_space.
                    blank_space += " "
                
                for y in range(1,5): #creates the column item surrounded by the relevant blank space and a "|"
                    rows[y + 1] += f"{blank_space}{results[x][y]}{blank_space}|"
                
                if len(results[x]) == 9: #just like above, adds the extra rows if there is three variables
                    for y in range(6,10): #creates the column item surrounded by the relevant blank space and a "|"
                        rows[y + 1] += f"{blank_space}{results[x][y]}{blank_space}|"