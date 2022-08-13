'''
EECS 210 -- Programming Assignment #1
Author: Jacob Wilkus
KUID: 3020877
'''

#The main() function for the program. Simply handles the calling of table() for each equation.
def main():
    #Calls the table() function for the 6 equations. The value of each equation is hardcoded to an integer in the order of the Assignment Worksheet. (So De Morgan's First Law is 0, Second Law is 1, etc.)
    for x in range(0,6):
        table(function)

#The table() function. Passes through which equation it is outputting to the data() function, and then takes the results from data() to fill out the table. It then prints those results!
def table(function):
    results = data(function)

#Takes in a function name, does math to determine the values for the truth table.
def data(function):
    #Basic variables needed to make the code function. 'results' is the output. 'names' are the hardcoded names. p, q, and r are lists with both possible states.
    results = []
    names = ["== De Morgan's First Law ==", "== De Morgan's Second Law ==", "== First Associative Law ==", "== Second Associative Law ==", "== [(p + q) * (p -> r) * (p -> r)] -> r = T ==", "== p <-> q = (p -> q) * (q -> p) =="]
    
    results.append(names[function]) #Assigns to results[0] the hardcoded name of the truth table, used later when printing.

    if function == 0: #code for De Morgan's First Law. -(p and q) = -p or -q.
        results.append(["p", False, False, True, True]) #column for p
        results.append(["q", False, True, False, True]) #column for q
        #results[3], results[4], results[5], results[6], results[7] = ["-p"], ["-q"], ["p * q"], ["-(p * q)"], ["-p + -q"] #creates the lists for each following column. Hardcodes the column title.

        results.append(negate(results[1])) #column for -p
        results.append(negate(results[2])) #column for -q

        for x in p:
            for y in q:
                results[5].append(x and y) #column for (p * q)

        results.append(negate(results[5])) #column for -(p * q)

#Takes a column of values and generates it's negated form. So p becomes -p.    
def negate(list):
    result = [] #Blank list that is filled out, then returned.
    for item in list:
        if item != True or item != False: #For the name value (list[0]), it handles the creation of the new, correct name.
            result.append("-" + item)
        else:
            result.append(not item) #appends the opposite value for the rest in order to do negation
    return result

def compare(list1,list2,function):
    result = []
    result.append(f"({list1[0]} {function} {list2[0]})") #creates the name, adds parantheses surrounding it.

    #creates temporary lists that clone list1 and list2. Removes the name value as it is unnecessary.
    temp1 = list1
    temp2 = list2
    temp1.pop(0)
    temp2.pop(0)

    #FINISH THIS JACOB!
    for x in temp1:
        for y in temp2:
            if function == "*":
                result.append(x and y)

if __name__ == "__main__":
    main()