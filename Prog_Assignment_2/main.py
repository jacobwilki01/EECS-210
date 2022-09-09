'''
Code Name: EECS 210 - Programming Assignment #2
Description: Runs the necessary code for proving or disproving each of predicates or quantifiers posed. 

Programmer: Jacob Wilkus
Date Created: September 1st, 2022

Preconditions and Postconditions:
    - main()
        - Takes in nothing. 
        - Runs at the start of the code. 
        - Calls each of the relevant question functions.
        - Returns nothing.
        - Prints all of the results.
    - equation functions:
        - universal(list)
            - takes in a list of truth values
            - returns a boolean value of the value of the universal quantifier for the given list.
        - existential(list)
            - takes in a list of truth values
            - returns a boolean value of the value of the existential quantifier for the given list.
        - disjunction(list1,list2)
            - takes in 2 lists of truth values and compares them against each other
            - returns a singular list of the comparison results.
        - negation(input)
            - Takes in either a boolean or list of truth values
            - Returns the opposite boolean or an inverse list.
        - compare(val1,val2)
            - compares two integers using less than.
            - returns a boolean depending on the result
        - if_zero(val1,val2)
            - takes in two integers, and checks if one of them is zero by multiplying them together
            - returns a boolean depending on the result of the multiplication
    - proof functions:
        - proof(mode,function,values)
            - takes in a 'mode' string, 'function' string, and a 'values' list.
            - the 'mode' determines if we are proving the existential quantifier or universal quantifier.
            - the 'function' string is the words used to describe what the function is
            - the 'values' list is iterated over to determine if the quantifiers hold true
            - returns a string that includes proves the given function is either True or False.
        - proof_large(mode,comp,func1,func2,values)
            - same as proof(), except it takes in two functions ('func1' and 'func2') and a function comparison ('comp').
            - returns a string that proves the given comparison beween the two functions is either True or False.
        - proof_nested(mode_x,mode_y,values)
            - same as proof() except it has two 'modes' ('mode_x' and 'mode_y') based on the two modes for nested quantifiers.
            - returns a string that proves the nested quantifier either True or False based on the given modes.
        - proof_demo(mode1,mode2,function,values)
            - same as proof(), except for proving De Morgan's Law.
            - has two modes, but compared to proof_nested, the 'mode1' refers to whether we are dealing with the negation or equivalent, and mode2 is if the given quantifier is existential or universal.
            - returns a string that proves De Morgan's Law True for the relevant negation and equivalent quantifier.
    - question functions: one_a(), one_b(), one_c(), one_d(), one_e(), one_f(), two_a(), two_b(), two_c(), two_d()
        - takes in nothing
        - called by main()
        - returns a string that consists of a boolean for whether the certain equation is True or False, and the relevant proof function (as described above).
'''

#The main() function for the program. Simply calls each of the relevant question functions.
def main():
    #Creates a list of all of the functions listed under #1 on the assignment sheet. Iterates over that list, calling them all, and prints their result.
    one = [one_a(),one_b(),one_c(),one_d(),one_e(),one_f()]
    for letter in one:
        print(letter)

    print("") #Prints a simple blank line to separate the answers to #1 and #2.

    #Creates a list of all of the functions listed under #2 on the assignment sheet. Iterates over that list, calling them all, and prints their result.
    two = [two_a(),two_b(),two_c(),two_d()]
    for letter in two:
        print(letter)

#Function for universal.
def universal(list):
    for value in list: #iterates over the values of an inputted list.
        if value == False: #if one False exists, the function returns False.
            return False
    return True #if no Falses exist, the function returns True

#Function for existential.
def existential(list):
    for value in list: #iterates over the values of an inputted list.
        if value == True: #if one True exists, the function returns True.
            return True
    return False #if no Trues exist, the function returns False.

#Function for disjunction.
def disjunction(list1,list2):
    result = [] #creates a blank list that will be appended to with results.
    for x in range(0,len(list1)): #iterates over the indexes of both lists. Iterates over the indexes rather than the items in the list so we can also easily access list2.
        if not (list1[x] or list2[x]): #compares the value in each index of list1 and list2 using or. If neither is true, appends a False to the list.
            result.append(False)
        else:
            result.append(True) #if one of them is True, it appends a True.
    
    return result #Once iteration is complete, it returns the result list.

#Function for negation.
def negation(input):
    if input == True or input == False: #checks if the input is either a boolean or list.
        return not input #if it's a boolean, it returns the opposite of the input.
    else: #if it's a list, it does the following code.
        result = [] #creates a new, blank list, to append results to.
        for item in input: #iterates over the input list, and appends the opposite of each item to the result list.
            result.append(not item)
        return result #once the iteration is finished, it returns the result list.

#Function for comparison.
def compare(val1,val2):
    if val1 < val2: #checks if the first value is less than the second, returns a boolean representing the result.
        return True
    else:
        return False

#Function for checking if one or more of the values are zero.
def if_zero(val1,val2):
    if val1 * val2 == 0: #checks if either of the values are zero by multiplying them together and seeing if the product equals 0, returns a boolean representing the result.
        return True
    else:
        return False

#Function for proving simple comparisons.
def proof(mode,function,values):
    if mode == "exis": #checks 'mode' to see if we are in existential mode. runs the following if True.
        for val in range(0,len(values)): #iterates over the indexes of the inputted values.
            if values[val] == True: #checks if at least one of them is True.
                return f"{val} {function}" #if one of them is true, it returns a string explaining why. Ex: "0 is less than 2"
        return f"there exists no value where x {function}" #if no items are true, it returns a string explaining why.
    elif mode == "univ": #checks 'mode' to see if we are in universal mode. runs the following if True.
        for val in range(0,len(values)): #iterates over the indexes of the inputted values.
            if values[val] == False: #checks if at least one of them is False.
                return f"{val} is not {function}" #if one of them is False, it returns a string explaining why. Ex: "2 is not less than 2"
        return f"all values in the range satisfy x {function}" #if they are all True, it returns a string explaining that.

#Function for proving comparisons between two functions.
def proof_large(mode,comp,func1,func2,values):
    if mode == "exis": #checks 'mode' to see if we are in existential mode. runs the following if True.
        for val in range(0,len(values)): #iterates over the indexes of the inputted values.
            if values[val] == True: #checks if at least one of them is True.
                return f"{val} is either {func1} {comp} {func2}" #if one of them is true, it returns a string explaining why. Ex: "0 is either less than 2 or greater than 5"
        return f"there exists no value where x {func1} {comp} {func2}" #if no items are true, it returns a string explaining why.
    elif mode == "univ": #checks 'mode' to see if we are in universal mode. runs the following if True.
        for val in range(0,len(values)): #iterates over the indexes of the inputted values.
            if values[val] == False: #checks if at least one of them is False.
                return f"{val} is not {func1} {comp} {func2}" #if one of them is False, it returns a string explaining why. Ex: "2 is not less than 2 or greater than 5"
        return f"all values in the range satisfy x {func1} {comp} {func2}" #if they are all True, it returns a string explaining that.

#Function for proving a nested quantifier. Extremely long, so bear with me...
def proof_nested(mode_x,mode_y,values):
    values_x, values_y = [], [] #creates blank lists used to determine all values of x and y.

    if mode_x == "exis" and mode_y == "exis": #runs the following code if both x and y are existential
        for val in range(0,len(values)): #iterates over the indexes of the inputted values list
            if values[val] == True: #if any of the values in values are true, it runs the following code
                values_x.append(val // 11) #appends simply the index divided by 11, without the remainder, representing which x value it is on
                values_y.append(val - (11 * (val // 11))) #appends a mini math equation to determine the subsequent y value, which is the difference between val and the x value * 11.
    elif mode_x == "univ" and mode_y == "univ": #runs the following code if both x and y are universal
        for val in range(0,len(values)): #iterates over the indexes of the inputted values.
            if values[val] == False: #if any of the values are False, it runs the following code
                values_x.append(val // 11) #appends simply the index divided by 11, without the remainder, representing which x value it is on
                values_y.append(val - (11 * (val // 11))) #appends a mini math equation to determine the subsequent y value, which is the difference between val and the x value * 11.
    elif mode_x != mode_y: #if the modes are different, it runs the following code.
        if mode_x == "univ": #this runs if x is universal but y is existential
            for val in range(0,len(values)): #iterates over the indexes in values
                if values[val] == False: #if it's False, runs the following
                    values_x.append(val // 11) #appends the relevant x value to values_x
                elif values[val] == True: #if any are True, runs the following
                    values_y.append(val - (11 * (val // 11))) #appends the relevant y value to values_y
        elif mode_y == "univ": #this runs if y is universal but x is existential
            for val in range(0,len(values)): #iterates over the indexes in values
                if values[val] == False: #if any are False, runs the following
                    values_y.append(val // 11) #appends the relevant values to values_y
                elif values[val] == True: #if any are True, runs the following
                    values_x.append(val - (11 * (val // 11))) #appends the reelvant values to values_x

    #At this point in the code, no matter what modes were activated, we have two lists filled  with numerous sets of numbers, including duplicates

    if len(values_x) == 0 and len(values_y) == 0: #this checks if any values have been appended, which can happen if both are universal or existential.
        return f"all values in the range satisfy x * y = 0" #if there are not any values, returns this string.
    else: #if there are values, it runs the following
        sorted_x, sorted_y = [], [] #creates new lists to manipulate later
        for item in sorted(set(values_x)): #iterates over a sorted set of values_x, appends them to the new sorted_x list
            sorted_x.append(str(item))
        for item in sorted(set(values_y)): #iterates over a sorted set of values_y, appends them to the new sorted_y list
            sorted_y.append(str(item))
        
        #takes the now sorted lists, and turns them into usable strings to return with the delimiter " ,"
        delimiter = ", "
        return_x, return_y = delimiter.join(sorted_x), delimiter.join(sorted_y)
        
        #Determines the mode once again, and returns a string to prove the equation with the return_x and return_y values determined above.
        if mode_x == "exis" and mode_y == "exis":
            return f"x * y does equal 0 when x is {return_x} and y is 0. As well as when y is {return_y} and x is 0"
        elif mode_x == "univ" and mode_y == "univ":
            return f"x * y does not equal 0 when x is {return_x} and y is not zero. As well as when x is not zero and y is {return_y}"
        else:
            if mode_x == "univ":
                return f"x * y does not equal 0 when x is {return_x} and y is not 0"
            elif mode_y == "univ":
                return f"x * y does not equal 0 when y is {return_y} and x is not 0"

#Proof function for De Morgan's Law. 
def proof_demo(mode1,mode2,function,values):
    #Code is mostly the same as the other proof functions, with the exception of determining an extra mode value, which corresponds to which side of the equation it is (the "negation" and the "equivalent")
    #After it determines which side of the equation it is, it runs the exact same code as proof().
    if mode1 == "negate":
        if mode2 == "exis": #runs the following if mode2 is existential
            for val in range(0,len(values)): #iterates over the indexes in values
                if values[val] == False: #if any value in values is False, returns the following
                    return f"{val} is not {function}"
            return f"there exists no value where x is not {function}" #if no values are False, it returns this
        elif mode2 == "univ": #runs the following if mode2 is universal
            for val in range(0,len(values)): #iterates over the indexes in values
                if values[val] == True: #if any value is True, returns the following
                    return f"{val} is {function}"
            return f"all values in the range satisfy x {function}" #if no values are True, it returns this
    else:
        if mode2 == "exis": #runs the following if mode2 is existential
            for val in range(0,len(values)):#iterates over the indexes in values
                if values[val] == True: #if any value is True, returns the following
                    return f"{val} is {function}"
            return f"there exists no value where x is not {function}" #if no values are True, it returns this
        elif mode2 == "univ":
            for val in range(0,len(values)):#iterates over the indexes in values
                if values[val] == False: #if any value is False, returns the following
                    return f"{val} is not {function}"
            return f"all values in the range satisfy x {function}" #if no values are False, it returns this

#code for running question 1a.)
def one_a():
    result = [] #creates a blank list to determine the values
    for x in range(0,11): #iterates over numbers 0-10 and uses the compare function to compare them to 2
        result.append(compare(x,2))
    
    return f"1a.) {existential(result)} because {proof('exis','less than 2',result)}." #uses the previous functions to return a final string that prints in main()

#code for running 1b.)
def one_b():
    result = [] #creates a blank list to determine the values
    for x in range(0,11): #iterates over numbers 0-10 and uses the compare function to compare them to 2
        result.append(compare(x,2))

    return f"1b.) {universal(result)} because {proof('univ','less than 2',result)}." #uses the previous functions to return a final string that prints in main()

#code for running 1c.)
def one_c():
    result1,result2 = [],[] #creates two blank lists for determining the values
    for x in range(0,11): #iterates over numbers 0-10 and uses the compare function to compare them to 2 and 7
        result1.append(compare(x,2))
        result2.append(compare(7,x))
    
    #creates a variable that refers to the disjunction function
    final = disjunction(result1,result2)
    
    return f"1c.) {existential(final)} because {proof_large('exis','or','less than 2','greater than 7',final)}." #uses the previous functions to return a final string that prints in main()

#code for running 1d.)
def one_d():
    result1,result2 = [],[] #creates two blank lists for determining the values
    for x in range(0,11): #iterates over numbers 0-10 and uses the compare function to compare them to 2 and 7
        result1.append(compare(x,2))
        result2.append(compare(7,x))
    
    #creates a variable that refers to the disjunction function
    final = disjunction(result1,result2)
    
    return f"1d.) {universal(final)} because {proof_large('univ','or','less than 2','greater than 7',final)}." #uses the previous functions to return a final string that prints in main()

#code for running 1e.)
def one_e():
    result = [] #creates a blank list to determine the values
    for x in range(0,11):
        result.append(compare(x,5))
    
    #creates two vairables that refer to either side of the equation
    negate = negation(existential(result))
    equiv = universal(negation(result))

    #uses the previous functions to return a final string that prints in main()
    return f"1e.) De Morgan's Law holds {negate == equiv} because both -∃xP(x) is {negate} and ∀x(-P(x)) is {equiv}. -∃xP(x) is {negate} because {proof_demo('negate','exis','less than 5',result)} and ∀x(-P(x)) is {equiv} because {proof_demo('equiv','univ','less than 5',result)}."

#code for running 1f.)
def one_f():
    result = [] #creates a blank list to determine the values
    for x in range(0,11): #iterates over numbers 0-10 and uses the compare function to compare them to 5
        result.append(compare(x,5))
    
    #creates two vairables that refer to either side of the equation
    negate = negation(universal(result))
    equiv = existential(negation(result))

    #uses the previous functions to return a final string that prints in main()
    return f"1f.) De Morgan's Law holds {negate == equiv} because both -∀xP(x) is {negate} and ∃x(-P(x)) is {equiv}. -∀xP(x) is {negate} because {proof_demo('negate','univ','less than 5',result)} and ∃x(-P(x)) is {equiv} because {proof_demo('equiv','exis','less than 5',result)}."

#code for running 2a.)
def two_a():
    result = [] #creates a blank list to determine the values
    for x in range(0,11): #iterates over numbers 0-10 two times for x and y, and determines if either is zero using if_zero()
        for y in range(0,11):
            result.append(if_zero(x,y))

    return f"2a.) {universal(result)} because {proof_nested('univ','univ',result)}." #uses the previous functions to return a final string that prints in main()

#code for running 2b.)
def two_b():
    result = [] #creates a blank list to determine the values
    for x in range(0,11): #iterates over numbers 0-10 two times for x and y, and determines if either is zero using if_zero()
        for y in range(0,11):
            result.append(if_zero(x,y))

    return f"2b.) {universal(result)} because {proof_nested('univ','exis',result)}." #uses the previous functions to return a final string that prints in main()

#code for running 2c.)
def two_c():
    result = [] #creates a blank list to determine the values
    for x in range(0,11): #iterates over numbers 0-10 two times for x and y, and determines if either is zero using if_zero()
        for y in range(0,11):
            result.append(if_zero(x,y))

    return f"2c.) {universal(result)} because {proof_nested('exis','univ',result)}." #uses the previous functions to return a final string that prints in main()

#code for running 2d.)
def two_d():
    result = [] #creates a blank list to determine the values
    for x in range(0,11): #iterates over numbers 0-10 two times for x and y, and determines if either is zero using if_zero()
        for y in range(0,11):
            result.append(if_zero(x,y))

    return f"2d.) {existential(result)} because {proof_nested('exis','exis',result)}." #uses the previous functions to return a final string that prints in main()

#basic python code to run main()
if __name__ == "__main__":
    main()