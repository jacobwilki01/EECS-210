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

#Function for universal. Just iterataes over a list of truth values and determines if they are all true. Returns a boolean based on that iteration.
def universal(list):
    for value in list:
        if value == False:
            return False
    return True

#Function for existential. Just iterataes over a list of truth values and determines if they are all true. Returns a boolean based on that iteration.
def existential(list):
    for value in list:
        if value == True:
            return True
    return False

#Function for disjunction. Just iterataes over two lists of truth values and determines if either one or the other is true. Returns a list of truth values based on that iteration.
def disjunction(list1,list2):
    result = []
    for x in range(0,len(list1)):
        if not (list1[x] or list2[x]):
            result.append(False)
        else:
            result.append(True)
    
    return result

def negation(input):
    if input == True or input == False:
        return not input
    else:
        result = []
        for item in input:
            if item == True:
                result.append(False)
            else:
                result.append(True)
        return result

def compare(val1,val2):
    if val1 < val2:
        return True
    else:
        return False

def if_zero(val1,val2):
    if val1 * val2 == 0:
        return True
    else:
        return False

def proof(mode,function,values):
    if mode == "exis":
        for val in range(0,len(values)):
            if values[val] == True:
                return f"{val} {function}"
        return f"there exists no value where x {function}"
    elif mode == "univ":
        for val in range(0,len(values)):
            if values[val] == False:
                return f"{val} is not {function}"
        return f"all values in the range satisfy x {function}"

def proof_large(mode,comp,func1,func2,values):
    if mode == "exis":
        for val in range(0,len(values)):
            if values[val] == True:
                return f"{val} is either {func1} {comp} {func2}"
        return f"there exists no value where x {func1} {comp} {func2}"
    elif mode == "univ":
        for val in range(0,len(values)):
            if values[val] == False:
                return f"{val} is not {func1} {comp} {func2}"
        return f"all values in the range satisfy x {func1} {comp} {func2}"

def proof_nested(mode_x,mode_y,values):
    values_x, values_y = [], []

    if mode_x == "exis" and mode_y == "exis":
        for val in range(0,len(values)):
            if values[val] == True:
                values_x.append(val // 11)
                values_y.append(val - (11 * (val // 11)))
    elif mode_x == "univ" and mode_y == "univ":
        for val in range(0,len(values)):
            if values[val] == False:
                values_x.append(val // 11)
                values_y.append(val - (11 * (val // 11)))
    elif mode_x != mode_y:
        if mode_x == "univ":
            for val in range(0,len(values)):
                if values[val] == False:
                    values_x.append(val // 11)
                elif values[val] == True:
                    values_y.append(val - (11 * (val // 11)))
        elif mode_y == "univ":
            for val in range(0,len(values)):
                if values[val] == False:
                    values_y.append(val // 11)
                elif values[val] == True:
                    values_x.append(val - (11 * (val // 11)))

    if len(values_x) == 0 and len(values_y) == 0:
        return f"all values in the range satisfy x * y = 0"
    else:
        sorted_x, sorted_y = [], []
        for item in sorted(set(values_x)):
            sorted_x.append(str(item))
        for item in sorted(set(values_y)):
            sorted_y.append(str(item))
            
        delimiter = ", "
        return_x, return_y = delimiter.join(sorted_x), delimiter.join(sorted_y)
        
        if mode_x == "exis" and mode_y == "exis":
            return f"x * y does equal 0 when x is {return_x} and y is 0. As well as when y is {return_y} and x is 0"
        elif mode_x == "univ" and mode_y == "univ":
            return f"x * y does not equal 0 when x is {return_x} and y is not zero. As well as when x is not zero and y is {return_y}"
        else:
            if mode_x == "univ":
                return f"x * y does not equal 0 when x is {return_x} and y is not 0"
            elif mode_y == "univ":
                return f"x * y does not equal 0 when y is {return_y} and x is not 0"

def proof_demo(mode1,mode2,function,values):
    if mode1 == "negate":
        if mode2 == "exis":
            for val in range(0,len(values)):
                if values[val] == False:
                    return f"{val} is not {function}"
            return f"there exists no value where x is not {function}"
        elif mode2 == "univ":
            for val in range(0,len(values)):
                if values[val] == True:
                    return f"{val} is {function}"
            return f"all values in the range satisfy x {function}"
    else:
        if mode2 == "exis":
            for val in range(0,len(values)):
                if values[val] == True:
                    return f"{val} is {function}"
            return f"there exists no value where x is not {function}"
        elif mode2 == "univ":
            for val in range(0,len(values)):
                if values[val] == False:
                    return f"{val} is not {function}"
            return f"all values in the range satisfy x {function}"

def one_a():
    result = []
    for x in range(0,11):
        result.append(compare(x,2))
    
    return f"1a.) {existential(result)} because {proof('exis','less than 2',result)}."

def one_b():
    result = []
    for x in range(0,11):
        result.append(compare(x,2))

    return f"1b.) {universal(result)} because {proof('univ','less than 2',result)}."

def one_c():
    result1,result2 = [],[]
    for x in range(0,11):
        result1.append(compare(x,2))
        result2.append(compare(7,x))
    
    final = disjunction(result1,result2)
    
    return f"1c.) {existential(final)} because {proof_large('exis','or','less than 2','greater than 7',final)}."

def one_d():
    result1,result2 = [],[]
    for x in range(0,11):
        result1.append(compare(x,2))
        result2.append(compare(7,x))
    
    final = disjunction(result1,result2)
    
    return f"1d.) {universal(final)} because {proof_large('univ','or','less than 2','greater than 7',final)}."

def one_e(): #x<5
    result = []
    for x in range(0,11):
        result.append(compare(x,5))
    
    negate = negation(existential(result))
    equiv = universal(negation(result))

    return f"1e.) De Morgan's Law holds {negate == equiv} because both the negation is {negate} and the equivalent is {equiv}. The negation is {negate} because {proof_demo('negate','exis','less than 5',result)} and the equivalent is {equiv} because {proof_demo('equiv','univ','less than 5',result)}."

def one_f():
    result = []
    for x in range(0,11):
        result.append(compare(x,5))
    
    negate = negation(universal(result))
    equiv = existential(negation(result))

    return f"1f.) De Morgan's Law holds {negate == equiv} because both the negation is {negate} and the equivalent is {equiv}. The negation is {negate} because {proof_demo('negate','univ','less than 5',result)} and the equivalent is {equiv} because {proof_demo('equiv','exis','less than 5',result)}."


def two_a():
    result = []
    for x in range(0,11):
        for y in range(0,11):
            result.append(if_zero(x,y))

    return f"2a.) {universal(result)} because {proof_nested('univ','univ',result)}."

def two_b():
    result = []
    for x in range(0,11):
        for y in range(0,11):
            result.append(if_zero(x,y))

    return f"2b.) {universal(result)} because {proof_nested('univ','exis',result)}."

def two_c():
    result = []
    for x in range(0,11):
        for y in range(0,11):
            result.append(if_zero(x,y))

    return f"2c.) {universal(result)} because {proof_nested('exis','univ',result)}."

def two_d():
    result = []
    for x in range(0,11):
        for y in range(0,11):
            result.append(if_zero(x,y))

    return f"2d.) {existential(result)} because {proof_nested('exis','exis',result)}."

if __name__ == "__main__":
    main()