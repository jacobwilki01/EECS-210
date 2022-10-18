'''
Code Name: EECS 210 - Programming Assignment 5
Description: Runs the necessary code to check if a function is a function and if it is, what type of function it is.

Author: Jacob Wilkus
Date Created: October 13th, 2022

Preconditions and Postconditions:
    -main()
        -Takes in nothing.
        -Creates the necessary variables to run the code. (the a's, b's, and f's)
        -Calls is_func() and func_type() to check if the function is a function and what type of function it is.
        -Prints the results of the function.
    -is_func(a,f)
        -Takes in a list of elements that represents 'a' and a list of tuples that represents 'f'.
        -Checks if 'f' is a function by checking if every element in 'a' is in 'f' and if there is only one of each element in 'a' in 'f'.
        -Returns True if 'f' is a function and False if it is not.
    -func_type(b,f)
        -Takes in a list of elements that represents 'b' and a list of tuples that represents 'f'.
        -Checks if 'f' is injective by checking if every element in 'b' is in 'f' and if there is only one of each element in 'b' in 'f'.
        -Checks if 'f' is surjective by checking if every element in 'b' is in 'f'.
        -Returns a string that tells the user what type of function 'f' is.
    -inverse(f)
        -Takes in a list of tuples that represents 'f'.
        -Creates a list of tuples that represents the inverse of 'f'.
        -Returns the inverse of 'f'.
'''

#Checks if f is a function
def is_func(a,f):
    for i in a: #iterates through every element in a
        check = False #creates a variable to check if the element is in f
        times = 0 #creates a variable to check how many times the element is in f
        for j in f: #iterates through every tuple in f
            if i == j[0]: #checks if the element is in the x-value of the tuple
                check = True #sets check to True if the element is in the x-value of the tuple
                times += 1 #adds 1 to times if the element is in the x-value of the tuple 
        if not check or times > 1: #checks if the element is not in f or if the element is in f more than once
            return False #returns False if the element is not in f or if the element is in f more than once
    
    return True #returns True if every element in a is in f and if there is only one of each element in a in f

#Checks if f is injective, surjective, bijective, or none.
def func_type(b,f):
    for i in b: #iterates through every element in b
        times = 0 #creates a variable to check how many times the element is in f
        for j in f: #iterates through every tuple in f
            if i == j[1]: #checks if the element is in the y-value of the tuple
                times += 1 #adds 1 to times if the element is in the y-value of the tuple
        if times == 1: #checks if the element is in f only once
            is_inj = True #sets is_inj to True if the element is in f only once
        elif times > 1: #checks if the element is in f more than once
            is_inj = False #sets is_inj to False if the element is in f more than once
            break #breaks the loop if the element is in f more than once
    
    is_sur = True #creates a variable to check if f is surjective
    for i in b: #iterates through every element in b
        times = 0 #creates a variable to check how many times the element is in f
        for j in f: #iterates through every tuple in f
            if i == j[1]: #checks if the element is in the y-value of the tuple
                times += 1 #adds 1 to times if the element is in the y-value of the tuple
        if times == 0: #checks if the element is not in f
            is_sur = False #sets is_sur to False if the element is not in f
            break #breaks the loop if the element is not in f

    if is_inj: #checks if f is injective
        if is_sur: #checks if f is surjective
            return f"bijective with an inverse function of: {inverse(f)}" #returns a string that tells the user that f is bijective and gives the inverse of f
        else: #checks if f is not surjective
            return "injective" #returns a string that tells the user that f is injective
    elif is_sur: #checks if f is surjective
        return "surjective" #returns a string that tells the user that f is surjective
    else: #checks if f is not injective or surjective
        return "neither injective nor surjective" #returns a string that tells the user that f is neither injective nor surjective

#Returns the inverse of f
def inverse(f):
    inverse = [] #creates a list to store the inverse of f
    for i in f: #iterates through every tuple in f
        inverse.append((i[1],i[0])) #adds the inverse of the tuple to inverse
    
    return inverse #returns the inverse of f

def main():
    #Creates the necessary variables to run the code. (the a's, b's, and f's)
    a1, a2 = ['a','b','c','d'], ['a','b','c']
    b1, b2, b3, b4, b5, b6 = ['v','w','x','y','z'], ['x','y','z'], ['w','x','y','z'], [1,2,3,4,5], [1,2,3,4], [1,2,3]
    f1, f2, f3, f4, f5, f6, f7, f8, f9 = [('a','z'),('b','y'),('c','x'),('d','w')], [('a','z'),('b','y'),('c','x'),('d','z')], [('a','z'),('b','y'),('c','x'),('d','w')], [('a',4),('b',5),('c',1),('d',3)], [('a',3),('b',4),('c',1)], [('a',2),('b',1),('c',3),('d',2)], [('a',4),('b',1),('c',3),('d',2)], [('a',2),('b',1),('c',2),('d',3)], [('a',2),('b',1),('a',4),('c',3)]

    #Code for #1
    if is_func(a1,f1): #checks if f1 is a function
        print(f"1.) f is a function that is {func_type(b1,f1)}.") #prints a string that tells the user that f1 is a function and what type of function f1 is
    else: #checks if f1 is not a function
        print("1.) f is not a function.") #prints a string that tells the user that f1 is not a function
    
    #Code for #2
    if is_func(a1,f2): #checks if f2 is a function
        print(f"2.) f is a function that is {func_type(b2,f2)}.") #prints a string that tells the user that f2 is a function and what type of function f2 is
    else: #checks if f2 is not a function
        print("2.) f is not a function.") #prints a string that tells the user that f2 is not a function
    
    #Code for #3
    if is_func(a1,f3): #checks if f3 is a function
        print(f"3.) f is a function that is {func_type(b3,f3)}.") #prints a string that tells the user that f3 is a function and what type of function f3 is
    else: #checks if f3 is not a function
        print("3.) f is not a function.") #prints a string that tells the user that f3 is not a function
    
    #Code for #4
    if is_func(a1,f4): #checks if f4 is a function
        print(f"4.) f is a function that is {func_type(b4,f4)}.") #prints a string that tells the user that f4 is a function and what type of function f4 is
    else: #checks if f4 is not a function
        print("4.) f is not a function.") #prints a string that tells the user that f4 is not a function
    
    #Code for #5
    if is_func(a2,f5): #checks if f5 is a function
        print(f"5.) f is a function that is {func_type(b5,f5)}.") #prints a string that tells the user that f5 is a function and what type of function f5 is
    else: #checks if f5 is not a function
        print("5.) f is not a function.") #prints a string that tells the user that f5 is not a function
    
    #Code for #6
    if is_func(a1,f6): #checks if f6 is a function
        print(f"6.) f is a function that is {func_type(b6,f6)}.") #prints a string that tells the user that f6 is a function and what type of function f6 is
    else: #checks if f6 is not a function
        print("6.) f is not a function.") #prints a string that tells the user that f6 is not a function
    
    #Code for #7
    if is_func(a1,f7): #checks if f7 is a function
        print(f"7.) f is a function that is {func_type(b5,f7)}.") #prints a string that tells the user that f7 is a function and what type of function f7 is
    else: #checks if f7 is not a function
        print("7.) f is not a function.") #prints a string that tells the user that f7 is not a function
    
    #Code for #8
    if is_func(a1,f8): #checks if f8 is a function
        print(f"8.) f is a function that is {func_type(b5,f8)}.") #prints a string that tells the user that f8 is a function and what type of function f8 is
    else: #checks if f8 is not a function
        print("8.) f is not a function.") #prints a string that tells the user that f8 is not a function
    
    #Code for #9
    if is_func(a2,f9): #checks if f9 is a function
        print(f"9.) f is a function that is {func_type(b5,f9)}.") #prints a string that tells the user that f9 is a function and what type of function f9 is
    else: #checks if f9 is not a function
        print("9.) f is not a function.") #prints a string that tells the user that f9 is not a function

if __name__ == "__main__":
    main()