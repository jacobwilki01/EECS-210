'''
EECS 210 -- Programming Assignment #1
Author: Jacob Wilkus
KUID: 3020877
'''

#The main() function for the program. Simply handles the calling of table() for each equation.
def main():
    #Calls the table() function for the 6 equations. The value of each equation is hardcoded to an integer in the order of the Assignment Worksheet. (So De Morgan's First Law is 0, Second Law is 1, etc.)
    for x in range(0,6):
        table(x)

#The table() function. Passes through which equation it is outputting to the data() function, and then takes the results from data() to fill out the table. It then prints those results!
def table(function):
    results = data(function) #the results for each function using data()
    
    #following code handldes the printing of the tables
    for x in range(0, len(results)):
        if x == 0:
            print(f"\n{results[x]}") #prints the header of the table first, which is results[0]
        else:
            for y in range(1,len(results[x])): #turns the boolean values in the lists into a printable form of 'T' and 'F'.
                if results[x][y] == True:
                    results[x][y] = "T"
                else:
                    results[x][y] = "F"
            if x == 1: #for the first column, which is universally p, it creates each row of the table by creating a list of rows by iterating over the first set of results.
                rows = []
                for row in results[x]:
                    rows.append(f"| {row} |")
            else: #for the rest of the columns, it adds the data to the previously made rows.
                for y in range(0,len(results[x])): #iterates over each of the columns
                    space = ""
                    for _ in range(0,len(results[x][0]) // 2): #using the variables made above, this defines the blank space surrounding each 'T' and 'F' because they are not the same. Does this by taking the length of the item in row 1 // 2 and adding " " to a space variable.
                        space += " "
                    if y == 0:
                        rows[y] += f" {results[x][y]} |" #handles the create of the first row, which has different rules than the other rows because the blank space is always a length of 1.
                    else: #the following accounts for each of the value rows, including defining the blank space to make the table look good
                        if len(space) == 0:
                            rows[y] += f" {results[x][y]} |" #handles when the space variable equals zero, which happens when the length of the column title equals 1.
                        else:
                            if len(results[x][0]) % 2 == 0: #when the column title has an even length, the space variable is slightly larger than needed, so we only have one space in the concatenated string rather than two.
                                rows[y] += f" {space}{results[x][y]}{space}|"
                            else:
                                rows[y] += f" {space}{results[x][y]}{space} |"
    for row in rows:
        print(row)

#Takes in a hardcoded function value, does math to determine the values for the truth table.
def data(function):
    #Basic variables needed to make the code function. 'results' is the output. 'names' are the hardcoded names.
    results = []
    names = ["== De Morgan's First Law ==", "== De Morgan's Second Law ==", "== First Associative Law ==", "== Second Associative Law ==", "== [(p + q) * (p -> r) * (q -> r)] -> r = T ==", "== p <-> q = (p -> q) * (q -> p) =="]
    
    results.append(names[function]) #Assigns to results[0] the hardcoded name of the truth table, used later when printing.

    if function == 0: #code for De Morgan's First Law. -(p * q) = -p + -q.
        results.append(["p", False, False, True, True]) #column for p
        results.append(["q", False, True, False, True]) #column for q

        results.append(negate(results[1])) #column for -p
        results.append(negate(results[2])) #column for -q

        results.append(compare(results[1],results[2],"*")) #column for (p * q)
        results.append(negate(results[5])) #column for -(p * q)

        results.append(compare(results[3],results[4],"+")) #column for -p + -q

        results.append(compare(results[6],results[7],"=")) #final column. just present to show that the Law is true!
    
    elif function == 1: #code for De Morgan's Second Law. -(p + q) = -p * -q
        results.append(["p", False, False, True, True]) #column for p
        results.append(["q", False, True, False, True]) #column for q

        results.append(negate(results[1])) #column for -p
        results.append(negate(results[2])) #column for -q

        results.append(compare(results[1],results[2],"+")) #column for (p + q)
        results.append(negate(results[5])) #column for -(p + q)

        results.append(compare(results[3],results[4],"*")) #column for -p * -q

        results.append(compare(results[6],results[7],"=")) #final column. just present to show that the Law is true!
    
    elif function == 2: #code for the First Associative Law. (p * q) * r = p * (q * r)
        results.append(["p", False, False, False, False, True, True, True, True]) #column for p
        results.append(["q", False, False, True, True, False, False, True, True]) #column for q
        results.append(["r", False, True, False, True, False, True, False, True]) #column for r

        results.append(compare(results[1],results[2],"*")) #column for (p * q)
        results.append(compare(results[2],results[3],"*")) #column for (q * r)

        results.append(compare(results[4],results[3],"*")) #column for (p * q) * r
        results.append(compare(results[1],results[5],"*")) #column for p * (q * r)

        results.append(compare(results[6],results[7],"=")) #final column. just present to show that the Law is true!

    elif function == 3: #code for the Second Associative Law. (p + q) + r = p + (q + r)
        results.append(["p", False, False, False, False, True, True, True, True]) #column for p
        results.append(["q", False, False, True, True, False, False, True, True]) #column for q
        results.append(["r", False, True, False, True, False, True, False, True]) #column for r

        results.append(compare(results[1],results[2],"+")) #column for (p + q)
        results.append(compare(results[2],results[3],"+")) #column for (q + r)

        results.append(compare(results[4],results[3],"+")) #column for (p + q) + r
        results.append(compare(results[1],results[5],"+")) #column for p + (q + r)

        results.append(compare(results[6],results[7],"=")) #final column. just present to show that the Law is true!

    elif function == 4: #[(p + q) * (p -> r) * (q -> r)] -> r = T
        results.append(["p", False, False, False, False, True, True, True, True]) #column for p
        results.append(["q", False, False, True, True, False, False, True, True]) #column for q
        results.append(["r", False, True, False, True, False, True, False, True]) #column for r

        results.append(compare(results[1],results[2],"+")) #column for (p + q)

        results.append(compare(results[1],results[3],"->")) #column for (p -> r)
        results.append(compare(results[2],results[3],"->")) #column for (q -> r)

        results.append(compare(results[4],results[5],"*",results[6])) #column for [(p + q) * (p -> r) * (q -> r)]

        results.append(compare(results[7],results[3],"->")) #[(p + q) * (p -> r) * (q -> r)] -> r

        results.append(compare(results[8],["T", True, True, True, True, True, True, True, True],"=")) #final column. Uses a list of all True to represent "T" in the equation.

    elif function == 5: #p <-> q = (p -> q) * (q -> p)
        results.append(["p", False, False, True, True]) #column for p
        results.append(["q", False, True, False, True]) #column for q

        results.append(compare(results[1],results[2],"<->")) #column for p <-> q

        results.append(compare(results[1],results[2],"->")) #column for (p -> q)
        results.append(compare(results[2],results[1],"->")) #column for (q -> p)

        results.append(compare(results[4],results[5],"*")) #column for (p -> q) * (q -> p)

        results.append(compare(results[3],results[6],"=")) #final column. Should be all Trues if I didn't mess up!

    return results #returns the values of all of the columns to be printed.

#Takes a column of values and generates it's negated form. So p becomes -p.    
def negate(list):
    result = [] #Blank list that is filled out, then returned.
    for item in list:
        if item != True and item != False: #For the name value (list[0]), it handles the creation of the new, correct name.
            result.append("-" + item)
        else:
            result.append(not item) #appends the opposite value for the rest in order to do negation
    return result #returns the final list to be used later

def compare(list1,list2,function,list3=None):
    result = []
    result.append(name(list1,list2,list3,function))

    for x in range(0,len(list1)): #runs the comparison for each value in the first list. Does this by iterating over the length of the list, and calling on the specific index
        if x == 0:
            pass #skips the 0 index of each list as it is the name
        else:
            if function == "*": #runs the comparison code if the function is conjunction
                if list3 == None:
                    result.append(list1[x] and list2[x])
                else:
                    result.append(list1[x] and list2[x] and list3[x])
            elif function == "+": #runs the comparison code if the function is disjunction
                result.append(list1[x] or list2[x])
            elif function == "->": #runs the comparison code if the function is implication, does so by returning True for every instance that isn't 'True then False'.
                if not (list1[x] == True and list2[x] == False):
                    result.append(True)
                else:
                    result.append(False)
            elif function == "<->": #runs the comparison code if the function is biconditional, does so by checking if each index is equivalent.
                if list1[x] == list2[x]:
                    result.append(True)
                else:
                    result.append(False)
            elif function == "=": #runs the comparison code if the function is equivalence. Simply checks if they are equivalent. If I did everything right, they should be!
                if list1[x] == list2[x]:
                    result.append(True)
                else:
                    result.append(False)
    
    return result #returns the final list to be used later

#The following function creates the name of the column and sets the relevant amount of parantheses.
def name(list1,list2,list3,function):
    #This one checks the name of the first input, if it not a single variable it adds parantheses
    if len(list1[0]) > 1:
        part1 = f"({list1[0]})"
    else:
        part1 = f"{list1[0]}"

    #This one checks the name of the second input, if it not a single variable it adds parantheses
    if len(list2[0]) > 1:
        part2 = f"({list2[0]})"
    else:
        part2 = f"{list2[0]}"

    #This checks if list3 exists, because it only exists in one instance. If it doesn't, then it returns the name between part1 and part2. If it exists, it does the convention for list3 and returns the name for all three!
    if list3 != None:
        #This one checks the name of the third input, if it not a single variable it adds parantheses
        if len(list3[0]) > 1:
            part3 = f"({list3[0]})"
        else:
            part3 = f"{list3[0]}"
        return f"{part1} {function} {part2} {function} {part3}"
    else:
        return f"{part1} {function} {part2}"

if __name__ == "__main__": #basic python terminology to start the program and call main() if and only if it is the origin program
    main()