'''
Code Name: EECS 210 - Programming Assignment #4
Description: Runs the necessary code for determining the state of relations, if they are equivalence relations, and if they are posets.

Programmer: Jacob Wilkus
Date Created: October 6th, 2022

Preconditions and Postconditions:
    -main()
        -Takes in nothing. Called immediately when the code is first run.
        -Creates numerous lists that represent sets and relations, puts them into the question functions, and prints their results.
    -operation functions (reflexive(relation,set); symmetric(relation); antisymmetric(relation); transitive(relation))
        -All takes in a relation, only reflexive also takes in a set.
        -Runs the relevant code to determine if the relation (and set) is the certain state, returns a boolean representing that
    -print_rel()
        -Takes in a relation in the form of a list.
        -Returns a string that formats it using { and } instead of [ and ].
    -closure functions (rel_close(set,relation); symm_close(relation); trans_close(relation))
        -Takes in a relation (or a set as well, if reflexive) and runs the same code as the original operation functions
        -Runs through them, and finds the pairs necessary to make the relation meet the criteria to be the certain state
        -Returns that list.
    -question functions (one(relation,set); two(relation); three(relation); four(relation,set); five(relation,set))
        -All takes in a relation, some also take in a set.
        -Checks the relevant state for the question, and returns a string representing the answer that will be printed in main()
        -Calls the operation and closure functions and print_rel() as needed.
'''

#main function for calling all of the question functions
def main():
    #Next lines create the relevant code for answering #1, creating two relations and sets.
    r1, s1 = [(1,1),(4,4),(2,2),(3,3)], [1,2,3,4]
    r2, s2 = [('a','a'),('c','c')], ['a','b','c','d']

    #The relevant code calling one(relation,set) for each inquiry, and printing the result
    print(one(r1,s1)) #one_d
    print(one(r2,s2)) #one_e

    #next line creates the relevant code for answering #2, creating two relations in the form of lists.
    r3, r4 = [(1,2), (4,4), (2,1), (3,3)], [(1,2), (3,3)]

    #The relevant code for calling two(relation) for each inquiry, printing the result.
    print(two(r3)) #two_d
    print(two(r4)) #two_e

    #The relevant code for answering #3. Creates two relations as lists.
    r5, r6 = [('a','b'), ('d','d'), ('b','c'), ('a','c')], [(1,1),(1,3),(2,2),(3,1),(3,2)]

    #The relevant code for calling three(relation) for each inquiry and printing the result.
    print(three(r5)) #three_d
    print(three(r6)) #three_e

    #The relevant code for answering #4 and #5. Creates two new relations and two new sets as lists to be used.
    r7, s3 = [(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)], [1, 2, 3, 4]
    r8, s4 = [(0, 0), (0, 1), (0, 2), (0, 3), (1,0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)], [0, 1, 2, 3]

    #The relevant code for calling four(relation,set) for each inquirt and printing the result.
    print(four(r7,s3)) #four_d
    print(four(r8,s4)) #four_e

    #The relevant code for calling five(relation,set) for each inquiry and printing the result.
    print(five(r7,s3)) #five_e
    print(five(r8,s4)) #five_f

#Code for reflexive(relation,set). Takes in two lists.
def reflexive(relation,set):
    #iterates over the set
    for value in set:
        check = False #for each iteration over the set, it redefines "check" to False.
        for pair in relation: #iterates over the relation
            if pair == (value,value): #if any pair in the relation is equal to (x,x) for the x value in the set, it turns check to True.
                check = True
        if not check: #if, at the end of all of the iteration over the relation, check is still False, it breaks the loop.
            break
    
    return check #returns True or False. If it's reflexive, check's final state is True when the loop ends.

#The relevant code for symmetric(relation). Takes in a relation as a list.
def symmetric(relation):
    for x in relation: #iterates over each value in the relation.
        check = False #for each iteration over the relation, sets check to False.
        for y in relation: #iterates over the relation a second time
            if y == (x[1],x[0]): #checks if any pair is equal to the reverse of the first in the relation, if so, changes check to True
                check = True 
        if not check: #if the whole second iteration results in check remaining False, it breaks the first loop.
            break

    return check #returns True or False.  If it's symmetric, check's final state is True when the loop ends.

#The relevant code for running antisymmetric(relation).
def antisymmetric(relation):
    if not symmetric(relation): #checks if the relation is not symmetric.
        for x in relation: #iterates over the relation once
            check = True #resets check to True for each iteration
            for y in relation: #iterations over the relation a second time
                if y == (x[1],x[0]) and x[0] != x[1]: #checks if there is a single, non-reflexive, value pair in the relation that makes it symmetric. If so, it turns check to False.
                    check = False
            if not check: #if the second iteration results in a False, it breaks the first loop.
                break

        return check #returns True or False. If it's antisymmetric, check's final state is True when the loop ends.
    else: #if the relation is symmetric, it automatically returns False, as a relation cannot be both symmetric and antisymmetric.
        return False

#relevant code for running transitive(relation)
def transitive(relation):
    temp = [] #creates a new, temp list
    for pair in relation: #iterates over the relation and appends every pair that does not have the same x and y value to temp.
        if pair[0] != pair[1]:
            temp.append(pair)
    
    for x in temp: #iterates over each pair in temp.
        check = False #for each iteration, sets check to False
        for y in temp: #iterates over temp a second time.
            if x[1] == y[0]: #checks if it meets the first criteria for transitive, which is that the first y-value is equal to the second x-value.
                for z in temp: #then iterates over a third time
                    if z == (x[0],y[1]): #checks if there exists a pair in the list satisfying the second criteria of transitive. If so, it sets check to True and removes all the values from the list in order to check for others.
                        check = True
                        temp.remove(x)
                        temp.remove(y)
                        temp.remove(z)
        if not check: #if check is not changing to true after all of the nested iteration, it breaks the first loop.
            break

    return check #returns True or False. If it is transitive, the final state of check will be True.

#The relevant code for print_rel(relation), which basically just formats it into a readable string.
def print_rel(relation):
    result = "{" #creates a new 'result' string that starts with a {
    for x in range(0,len(relation)): #iterates over the indexes of indexes of the relation
        if x != len(relation) - 1: #checks if the index is not the final index, then concatenates the value pair with a comma to the result string.
            result += f"{relation[x]}, "
        else: #if it is the last index, it only concatenates the value pair.
            result += f"{relation[x]}"

    return result + "}" #returns the final string with a closing }.

#Relevant code for rel_code(set,relation). Defines the relfexive closure for a relation.
def rel_close(set,relation):
    closure = relation #Creates a new variable that points to relation.

    #runs the same code as reflexive(set,relation) except it doesn't break the loop if it's not reflexive, just appends to it.
    for value in set: #iterates over the set.
        check = False #sets check to False for each iteration.
        for pair in relation: #iterates over the relation.
            if pair == (value,value): #checks if the pair is (x,x) for the relevant x from the set.
                check = True
        if not check: #if the pair does not exist, it appends it to the list.
            closure.append((value,value))
    
    return closure #returns that list.

#relevant code for generating a symmetric closure.
def symm_close(relation):
    closure = relation #creates a closure variable that points to the relation.
    for x in relation: #iterates over the relation
        check = False #for each iteration, sets check to False.
        for y in relation: #iterates over the relation again
            if y == (x[1],x[0]): #checks if a symmetric value exists. Changes check if so.
                check = True
        if not check: #if it does not exist, it appends it to closure.
            closure.append((x[1],x[0]))

    return closure #returns closure.

#The code for creating a transitive closure.
def trans_close(relation):
    temp, removed = [], [] #creates two blank lists.
    for pair in relation: #iterates over the relation, appends non-reflexive pairs to temp, the rest to removed.
        if pair[0] != pair[1]:
            temp.append(pair)
        else:
            removed.append(pair)
    
    #runs the same code as checking if its transitive, except it just appends to the code instead.
    for x in temp: #iterates over temp
        check = False #for each iteration, sets check to False
        for y in temp: #iterates a second time
            if x[1] == y[0]: #checks for the first transitive criteria
                for z in temp: #iterates a third time
                    if z != (x[0],y[1]) and x != z and y != z: #checks the second criteria
                        temp.append((x[0],y[1])) #appends if it doesn't exist
                        check = True #sets check to true, breaks the loop
                        break
        if check: #breaks the loop
            break
    
    for item in removed: #re-appends the items in removed
        temp.append(item)
    
    return sorted(set(temp)) #organizes and returns that list.

#relevant code for answering question #1
def one(relation,set):
    if reflexive(relation,set): #checks if the relation is reflexive
        return f"1a.) R = {print_rel(relation)}.\n1b.) R is reflexive.\n" #returns a string saying it is reflexive with the relation
    else:
        return f"1a.) R = {print_rel(relation)}.\n1b.) R is not reflexive.\n1c.) R* = {print_rel(rel_close(set,relation))}.\n" #returns a string saying it is not reflexive, the relation, and the reflexive closure.

#relevant code for answering question #2
def two(relation):
    if symmetric(relation): #checks if the relation is symmetric
        return f"2a.) R = {print_rel(relation)}.\n2b.) R is symmetric.\n" #returns a string saying it is symmetric with the relation
    else:
        return f"2a.) R = {print_rel(relation)}.\n2b.) R is not symmetric.\n2c.) R* = {print_rel(symm_close(relation))}.\n" #returns a string saying it is not symmetric, the relation, and the symmetric closure.

#relevant code for answering question #3
def three(relation):
    if transitive(relation): #checks if the relation is transitive
        return f"3a.) R = {print_rel(relation)}.\n3b.) R is transitive.\n" #returns a string saying it is transitive with the relation
    else:
        return f"3a.) R = {print_rel(relation)}.\n3b.) R is not transitive.\n3c.) R* = {print_rel(trans_close(relation))}.\n" #returns a string saying it is not transtive with the relation and transitive closure.

#relevant code for answering question #4
def four(relation, set):
    reflex, symm, trans = reflexive(relation, set), symmetric(relation), transitive(relation) #checks if the relation is reflexive, symmetric, and transitive.
    if reflex and symm and trans: #if all three are true, it returns a string saying it is an equivalence relation.
        return f"4a.) R = {print_rel(relation)}.\n4b.) R is an equivalence relation.\n"
    else: #if not, it returns a string saying it is not an equivalence relation and the reason why
        string = f"4a.) R = {print_rel(relation)}.\n4b.) R is not an equivalence relation.\n4c.) R is not an equivalence relation because it is "
        
        if not reflex: #checks if it is not reflexive
            if not symm: #checks if it is not symmetric
                if not trans: #checks if it is not transitive
                    string += f"not reflexive, symmetric, and transitive.\n" #if all three, it concatenates a string saying it is not reflexive, symmetric, and transitive.
                else:
                    string += f"not reflexive and symmetric.\n" #if transitive, it concatenates a string saying it is not reflexive and symmetric.
            else:
                if not trans: #checks if it is not transitive
                    string += f"not reflexive and transitve.\n" #concatenates a string saying it is not reflexive and transitive.
                else:
                    string += f"not reflexive.\n" #concatenates a string saying it is not reflexive.
        elif not symm: #checks if it is not symmetric
            if not trans: #checks if it is not transitive
                string += f"not symmetric and transitive.\n" #concatenates a string saying it is not symmetric and transitive.
            else:
                string += f"not symmetric.\n" #concatenates a string saying it is not symmetric.
        else:
            string += f"not transitive.\n" #concatenates a string saying it is not transitive.

        return string #returns the string.

#relevant code for answering question #5
def five(relation,set):
    reflex, antisymm, trans = reflexive(relation,set), antisymmetric(relation), transitive(relation) #checks if the relation is reflexive, antisymmetric, and transitive.
    if reflex and antisymm and trans: #if all three are true, it returns a string saying it is a partial order.
        return f"5a.) S = {print_rel(set)}.\n5b.) R = {print_rel(relation)}.\n5c.) (S,R) is a poset.\n"
    else: #if not, it returns a string saying it is not a partial order and the reason why
        string = f"5a.) S = {print_rel(set)}.\n5b.) R = {print_rel(relation)}.\n5c.) (S,R) is not a poset because it is "
        
        if not reflex: #checks if it is not reflexive
            if not antisymm: #checks if it is not antisymmetric
                if not trans: #checks if it is not transitive
                    string += f"not reflexive, antisymmetric, and transitive.\n" #if all three, it concatenates a string saying it is not reflexive, antisymmetric, and transitive.
                else:
                    string += f"not reflexive and antisymmetric.\n" #if transitive, it concatenates a string saying it is not reflexive and antisymmetric.
            else:
                if not trans: #checks if it is not transitive
                    string += f"not reflexive and transitve.\n" #concatenates a string saying it is
                else:
                    string += f"not reflexive.\n" #concatenates a string saying it is not reflexive.
        elif not antisymm: #checks if it is not antisymmetric
            if not trans: #checks if it is not transitive
                string += f"not antisymmetric and transitive.\n" #concatenates a string saying it is not
            else:
                string += f"not antisymmetric.\n" #concatenates a string saying it is not antisymmetric.
        else:
            string += f"not transitive.\n" #concatenates a string saying it is not transitive.

        return string #returns the string.

#relevant code for calling main()
if __name__ == "__main__":
    main()