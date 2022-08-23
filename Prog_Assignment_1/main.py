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
    
    #FIGURE OUT HOW TO DO THIS!

#Takes in a hardcoded function value, does math to determine the values for the truth table.
def data(function):
    #Basic variables needed to make the code function. 'results' is the output. 'names' are the hardcoded names.
    results = []
    names = ["== De Morgan's First Law ==", "== De Morgan's Second Law ==", "== First Associative Law ==", "== Second Associative Law ==", "== [(p + q) * (p -> r) * (p -> r)] -> r = T ==", "== p <-> q = (p -> q) * (q -> p) =="]
    
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

    elif function == 4: #[(p + q) * (p -> r) * (p -> r)] -> r = T
        results.append(["p", False, False, False, False, True, True, True, True]) #column for p
        results.append(["q", False, False, True, True, False, False, True, True]) #column for q
        results.append(["r", False, True, False, True, False, True, False, True]) #column for r

        results.append(compare(results[1],results[2],"+")) #column for (p + q)

        results.append(compare(results[1],results[3],"->")) #column for (p -> r)

        results.append(compare(results[4],results[5],"*")) #column for (p + q) * (p -> r). Not sure why the instructions has '* (p -> r) * (p -> r)' as it's redundant, so I'm using the easier form.

        results.append(compare(results[6],results[3],"->")) #[(p + q) * (p -> r)] -> r

        results.append(compare(results[7],["T", True, True, True, True, True, True, True, True],"=")) #final column. Uses a list of all True to represent "T" in the equation.

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

def compare(list1,list2,function):
    result = []
    if function != "=":
        result.append(f"({list1[0]} {function} {list2[0]})") #creates the name, adds parantheses surrounding it.
    else:
        result.append(f"{list1[0]} {function} {list2[0]}") #creates the name, but without the parantheses because they are not necessary for equivalence.
    
    for x in range(0,len(list1)): #runs the comparison for each value in the first list. Does this by iterating over the length of the list, and calling on the specific index
        if x == 0:
            pass #skips the 0 index of each list as it is the name
        else:
            if function == "*": #runs the comparison code if the function is conjunction
                result.append(list1[x] and list2[x])
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

if __name__ == "__main__": #basic python terminology to start the program and call main() if and only if it is the origin program
    main()