'''
Code Name: EECS 210 - Programming Assignment #3
Description: Runs the necessary code for creating relations, modifying them, and finding the characteristics of them.

Programmer: Jacob Wilkus
Date Created: September 20th, 2022

Preconditions and Postconditions:
    -main()
        -Takes in nothing
        -Calls all of the question functions, and inputs in the relative relations as lists.
        -Prints their outputs.
    -operation functions
        -union(rel1,rel2)
            -Creates the union of two relations
            -Takes in two relations in the form of lists
            -Appends all of their entries into a new list, then turns that list into a set to remove redundant values.
            -Then returns the set as a list using python's built-in sorted() function
        -intersect(rel1,rel2)
            -Creates the intersection of two relations
            -Takes in two relations in the form of lists
            -Iterates over the first relation, then for each iteration, iterates over the second.
            -Appends values to a new list for each iteration if the value in the first relation is equal to that in the second.
            -Returns that list.
        -diff(rel1,rel2)
            -Creates the difference between two relations
            -Takes in two relations in the form of lists
            -Iterates over the first relation, and appends them all to a new list.
            -Then does nested iteration over both relations, and removes values from the new list if they exist in both relation 1 and 2.
            -Returns that list.
        -compose(rel1,rel2)
            -Creates the composition of two relations
            -Takes in two relatons in the form of lists
            -Does nested iteration over both, and if the 'y' value of a given ordered pair in the first relation is the same as an 'x' value in a given ordered pair of the second, 
             it then appends to a new list an ordered pair containing the 'x' of the first relation's pair and the 'y' value of the second relation's pair.
            -returns that list
        -ordered_pair(set)
            -Creates the set of ordered pairs to use for #4.
            -Takes in a set in the form of a list.
            -Iterates over each value in it, and then iterates a second time. If the two relevant values are the same, it appends them in the form of an ordered pair to a new list.
            -Returns that new list.
        -reflex(set, relation)
            -Checks if a relation is reflexive
            -Takes in a set and a relation in the form of lists
            -Iterates over the given set and relation to see if any number in the set makes the relation not reflexive
            -Returns a string describing whether or not it is reflexive
        -symmetric(relation)
            -Checks if a releation is symmetric
            -Takes in a relation in the form of a list
            -Iterates over the given relation twice, and checks if the relation is reflexive
            -Returns a list signifying the result, and if it is False, the ordered pair that makes it false.
        -antisymmetric(relation)
            -Checks if a relation is antisymmetric
            -Follows the same code as symmetric(), except it returns the opposite results.
        -transitive(relation)
            -Checks if a relation is transitive
            -Takes in a relation in the form of a list
            -Does three levels of nested iteration to check that all three ordered pairs exist
            -Returns a string with information for if it is or is not transitive. If it is not, the string includes the relevant ordered pairs.
    -question functions: one_a(r1,r2), one_b(r1,r2), one_cr1,r2), one_d(r1,r2), two(r,s), three(r), four_a(set), four_b(set), four_c(set), four_d(set)
        -Takes in either a set, relation, or both. It may also take in two of one. All in the form of lists.
        -Calls on one of the operation functions above to determine the meat of the question.
        -Returns a string with the relevant results.
'''

#The main function for the program.
def main():
    #The following code answers the questions for #1.
    r1, r2 = [(1,1),(2,2),(3,3)], [(1,1),(1,2),(1,3),(1,4)] #Creates each of the relations as given in the assignment worksheet.
    one = [one_a,one_b,one_c,one_d] #Holds a list of each of the functions, that is then iterated over and each function is then called.
    for i in one:
        print(i(r1,r2)) #Prints the result of each question.

    #The following code answers questions 2 and 3.
    r, s = [(1,1),(1,4),(2,3),(3,1),(3,4)], [(1,0),(2,0),(3,1),(3,2),(4,1)] #Creates the relations R and S used for both questions.
    print(two(r,s)) #Calls on, and prints the result of two.
    print(three(r)) #Calls on, and prints the result of three.

    #The following code creates the set used in #4 by iterating from -10 to 10 and appending it to a list.
    four_set = []
    for x in range(-10,11):
        four_set.append(x)
    
    #The following code runs each of the relevant parts of #4.
    four = [four_a,four_b,four_c,four_d,four_e] #Holds a list of each of the functions, that is then iterated over and each function is then called.
    for i in four:
        print(i(four_set)) #Prints the result of each question.

#The following code is for the union() function.
def union(rel1,rel2):
    result = [] #Creates a blank list to hold the results of the function.
    for x in rel1: #iterates over the values in the first relation
        result.append(x) #appends those values to the new list.
        for y in rel2: #iterates over the values in the second relation
            result.append(y) #appends those values to the new list
    
    return sorted(set(result)) #returns the list sorted and with redundant items removed.

#Code for the intersect() function.
def intersect(rel1,rel2):
    result = [] #creates a blank list to hold the results of the function
    for x in rel1: #iterates over the items in the first relation
        for y in rel2: #iterates over the items in the second relation
            if x == y: #checks if the values are equal, then appends the value to the new list
                result.append(x)
    
    return result #returns that new list

#Code for the diff() function.
def diff(rel1,rel2):
    result = [] #creates a blank list to hold the result of the code
    for i in rel1: #iterates over the first relation, and appends each item to the new list
        result.append(i)

    for x in rel1: #iterates over the first relation
        for y in rel2: #iterates over the second relation
            if x == y: #if any of the values equal each other, it is removed from the list
                result.remove(x)
    
    return result #returns the list

#Code for the compose() function.
def compose(rel1,rel2):
    result = [] #Creates a blank list to hold the results
    for x in rel1: #iterates over the first relation
        for y in rel2: #iterates over the second relation
            if x[1] == y[0]: #if the 'y' value of the first pair, and the 'x' value of the second are the same, it runs the following
                result.append((x[0],y[1])) #appends an ordered pair of the 'x' value of the first pair and 'y' value of the second to the new list

    return result #returns the list

#Code the ordered_pair() function.
def ordered_pair(set):
    result = [] #creates a blank list to hold results.
    for x in set: #iterates over the set twice
        for y in set:
            if x + y == 0: #if each iteration value equals itself, it appends it to the new list.
                result.append((x,y))
    
    return result #returns that list.

#Code for the reflex() function.
def reflex(set, relation):
    #creates two new variables that are used to determine if the result is True.
    check = True 
    error = None

    #iterates over both the set and relation
    for num in set:
        for pair in relation:
            #checks if the each value of each ordered pair are both one value in the set. if they are not the same, it runs the following
            if (pair[0] != num and pair[1] == num) or (pair[1] != num and pair[0] == num): 
                check = False #turns the boolean above to False
                error = pair #makes the previously defined 'error' value hold the ordered pair that 'broke' it.
                break #breaks the relation iteration.
        if not check:
            break #breaks the set iteration.
    
    #determines what string to return. if it is reflexive, check = True. If not, the returned string includes error.
    if not check:
        return f"not reflexive because of {error}"
    else:
        return f"reflexive at all points."

#The code for the symmetric() function.
def symmetric(relation):
    error = None #creates a None variable that will be filled if the relation is not symmetric.
    for x in range(0,len(relation)): #iterates over the relation once
        check = False #for each iteration, it creates a new check variable that starts as False
        for y in range(0,len(relation)): #iterates over the relation a second time
            if relation[x] == (relation[y][1],relation[y][0]): #checks if the first ordered pair is the flip of the second
                check = True #if it is, it changes check to True
        if not check: #if the flip of a pair does not exist, it breaks the iteration and sets error to the pair that broke.
            error = relation[x]
            break
    
    #whether or not it is symmetric, it returns a list with that information that is either True or False in index 0, and the error value in index 1 if relevant.
    if not check:
        return [False,error]
    else:
        return [True]

#The code for the antisymmetric() function.
def antisymmetric(relation):
    error = None #creates a None variable that will be filled if the relation is not symmetric.
    for x in range(0,len(relation)): #iterates over the relation once
        check = True #for each iteration, it creates a new check variable that starts as True
        for y in range(0,len(relation)): #iterates over the relation a second time
            if relation[x] != (relation[y][1],relation[y][0]): #checks if the first ordered pair is the flip of the second
                check = False #if it is, it changes check to False
        if not check: #if it turns out to be False, it sets error to the pair that broke it and breaks the iteration.
            error = relation[x]
            break
    
    #whether or not it is antisymmetric, it returns a list with that information that is either True or False in index 0, and the error value in index 1 if relevant.
    if not check:
        return [False,error]
    else:
        return [True]

#Code for the transitive() function.
def transitive(relation):
    error1, error2, error3 = None, None, None #creates three None variables that, if the relation is not transitive, will refer the three ordered pairs necessary for the relation to be transitive.
    for x in range(0,len(relation)): #iterates over the relation's indexes
        check = False #creates a new 'check' variable each iteration
        for y in range(0,len(relation)): #iterates a second time
            if x != y: #runs the following only when x and y are not the same
                for z in range(0,len(relation)): #iterates a third time
                    if z != x and z != y: #only checks the following if z is not the same as x and y
                        if relation[z] != (relation[x][0],relation[y][1]): #if there doesn't exist a third pair to satisfy a transitive test, it runs the following
                            #maps the relevant variables to the ordered pairs and boolean value necessary, then breaks the iteration
                            check = True
                            error1 = relation[x]
                            error2 = relation[y]
                            error3 = (relation[x][0],relation[y][1])
                            break
        if check: #if check comes out as True, it breaks the top iteration.
            break
    
    #based on whether or not it is True, it returns a string with the relevant information.
    if check:
        return f"not transitive because {error3} does not exist to satisfy {error1} and {error2}"
    else:
        return f"transitive for all values in the set"

#Code for the one_a() function. Simply calls union() and returns a string to be printed.
def one_a(r1,r2): 
    return f"1a.) R1 ??? R2 = {union(r1,r2)}."

#Code for the one_b() function. Simply calls intersect() and returns a string to be printed.
def one_b(r1,r2):
    return f"1b.) R1 ??? R2 = {intersect(r1,r2)}."

#Code for the one_c() function. Simply calls diff() and returns a string to be printed.
def one_c(r1,r2):
    return f"1c.) R1 ??? R2 = {diff(r1,r2)}."

#Code for the one_d() function. Simply calls diff() and returns a string to be printed. Unlike one_c(), it flips the order of r1 and r2 in diff() as per the questio requirements
def one_d(r1,r2):
    return f"1d.) R2 ??? R1 = {diff(r2,r1)}."

#Code for the two() function. Simply calls compose() and returns a string to be printed.
def two(r,s):
    return f"2.) S ??? R = {compose(r,s)}."

#Code for the three() function. Simply calls compose() and returns a string to be printed.
def three(r):
    return f"3.) R^2 = {compose(r,r)}."

#Code for the four_a() function. Simply calls ordered_pair() and returns a string to be printed.
def four_a(set):
    return f"4a.) R has the following set of ordered pairs: {ordered_pair(set)}."

#Code for the four_a() function. Simply calls reflex() and returns a string to be printed.
def four_b(set):
    return f"4b.) R is {reflex(set,ordered_pair(set))}."

#Code for the four_c() function. Simply calls symmetric() on the ordered_pair() of the given set and returns a certain string based on it's result.
def four_c(set):
    result = symmetric(ordered_pair(set))
    if result[0]: #from the return of symmetric, 
        return f"4c.) R is symmetric for all values in the set."
    else:
        return f"4c.) R is not symmetric because of {result[1]}."

#Code for the four_d() function.
def four_d(set):
    result = symmetric(ordered_pair(set)) #first calls symmetric, because if the set is symmetric it cannot be antisymmetric
    if result[0]:
        return f"4d.) R is not antisymmetric because R is symmetric."
    else: #if it is not symmetric, it then checks if it is antisymmetric by calling antisymmetric(), and returns the relevant string to be printed.
        result2 = antisymmetric(ordered_pair(set))
        if result2[0]:
            return f"R is antisymmetric for all values in the set."
        else:
            return f"R is not antisymmetric because of {result2[1]}."

#Code for the four_a() function. Simply calls transitive() on the ordered_pair() of the given set and returns a string to be printed.
def four_e(set):
    return f"4e.) R is {transitive(ordered_pair(set))}."

#The default python syntax for making sure main() is called.
if __name__ == "__main__":
    main()