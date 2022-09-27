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
            -Takes in two relations in the form of lists
            -Appends all of their entries into a new list, then turns that list into a set to remove redundant values.
            -Then returns the set as a list using python's built-in sorted() function
        -intersect(rel1,rel2)
            -Takes in two relations in the form of lists
            -Iterates over the first relation, then for each iteration, iterates over the second.
            -Appends values to a new list for each iteration if the value in the first relation is equal to that in the second.
            -Returns that list.
        -diff(rel1,rel2)
            -Takes in two relations in the form of lists
            -Iterates over the first relation, and appends them all to a new list.
            -Then does nested iteration over both relations, and removes values from the new list if they exist in both relation 1 and 2.
            -Returns that list.
        -compose(rel1,rel2)
            -Takes in two relatons in the form of lists
            -Does nested iteration over both, and if the 'y' value of a given ordered pair in the first relation is the same as an 'x' value in a given ordered pair of the second, 
             it then appends to a new list an ordered pair containing the 'x' of the first relation's pair and the 'y' value of the second relation's pair.
            -returns that list
        -ordered_pair(set)
            -Takes in a set in the form of a list.
            -Iterates over each value in it, and then iterates a second time. If the two relevant values are the same, it appends them in the form of an ordered pair to a new list.
            -Returns that new list.
        -reflex(set, relation)
        -symmetric(relation)
        -antisymmetric(relation)
        -transitive(relation)
    -question functions: one_a(r1,r2), one_b(r1,r2), one_cr1,r2), one_d(r1,r2), two(r,s), three(r), four_a(set), four_b(set), four_c(set), four_d(set)
'''

def main():
    r1, r2 = [(1,1),(2,2),(3,3)], [(1,1),(1,2),(1,3),(1,4)]
    one = [one_a,one_b,one_c,one_d]
    for i in one:
        print(i(r1,r2))

    r, s = [(1,1),(1,4),(2,3),(3,1),(3,4)], [(1,0),(2,0),(3,1),(3,2),(4,1)]
    print(two(r,s))
    print(three(r))

    four_set = []
    for x in range(-10,11):
        four_set.append(x)
    
    four = [four_a,four_b,four_c,four_d,four_e]
    for i in four:
        print(i(four_set))

def union(rel1,rel2):
    result = []
    for x in rel1:
        result.append(x)
        for y in rel2:
            result.append(y)
    
    return sorted(set(result))

def intersect(rel1,rel2):
    result = []
    for x in rel1:
        for y in rel2:
            if x == y:
                result.append(x)
    
    return result

def diff(rel1,rel2):
    result = []
    for i in rel1:
        result.append(i)

    for x in rel1:
        for y in rel2:
            if x == y:
                result.remove(x)
    
    return result

def compose(rel1,rel2):
    result = []
    for x in rel1:
        for y in rel2:
            if x[1] == y[0]:
                result.append((x[0],y[1]))

    return result

def ordered_pair(set):
    result = []
    for x in set:
        for y in set:
            if x + y == 0:
                result.append((x,y))
    
    return result

def reflex(set, relation):
    check = True
    error = None
    for num in set:
        for pair in relation:
            if pair[0] != num or pair[1] != num:
                check = False
                error = pair
                break
        if not check:
            break
    
    if not check:
        return f"not reflexive because of {error}"
    else:
        return f"reflexive at all points."

def symmetric(relation):
    error = None
    for x in range(0,len(relation)):
        check = False
        for y in range(0,len(relation)):
            if relation[x] == (relation[y][1],relation[y][0]):
                check = True
        if not check:
            error = relation[x]
            break
    
    if not check:
        return [False,error]
    else:
        return [True]

def antisymmetric(relation):
    error = None
    for x in range(0,len(relation)):
        check = False
        for y in range(0,len(relation)):
            if relation[x] != (relation[y][1],relation[y][0]):
                check = True
        if not check:
            error = relation[x]
            break
    
    if not check:
        return [False,error]
    else:
        return [True]

def transitive(relation):
    error1, error2, error3 = None, None, None
    for x in range(0,len(relation)):
        check = False
        for y in range(0,len(relation)):
            if x != y:
                for z in range(0,len(relation)):
                    if z != x and z != y:
                        if relation[z] != (relation[x][0],relation[y][1]):
                            check = True
                            error1 = relation[x]
                            error2 = relation[y]
                            error3 = (relation[x][0],relation[y][1])
                            break
        if check:
            break
    
    if check:
        return f"not transitive because {error3} does not exist to satisfy {error1} and {error2}"
    else:
        return f"transitive for all values in the set"

def one_a(r1,r2):
    return f"1a.) R1 ∪ R2 = {union(r1,r2)}."

def one_b(r1,r2):
    return f"1b.) R1 ∩ R2 = {intersect(r1,r2)}."

def one_c(r1,r2):
    return f"1c.) R1 − R2 = {diff(r1,r2)}."

def one_d(r1,r2):
    return f"1d.) R2 − R1 = {diff(r2,r1)}."

def two(r,s):
    return f"2.) S ◦ R = {compose(r,s)}."

def three(r):
    return f"3.) R^2 = {compose(r,r)}."

def four_a(set):
    return f"4a.) R has the following set of ordered pairs: {ordered_pair(set)}."

def four_b(set):
    return f"4b.) R is {reflex(set,ordered_pair(set))}."

def four_c(set):
    result = symmetric(ordered_pair(set))
    if result[0]:
        return f"4c.) R is symmetric for all values in the set."
    else:
        return f"4c.) R is not symmetric because of {result[1]}."

def four_d(set):
    result = symmetric(ordered_pair(set))
    if result[0]:
        return f"4d.) R is not antisymmetric because R is symmetric."
    else:
        result2 = antisymmetric()
        if result2[0]:
            return f"R is antisymmetric for all values in the set."
        else:
            return f"R is not antisymmetric because of {result2[1]}."

def four_e(set):
    return f"4e.) R is {transitive(ordered_pair(set))}."

if __name__ == "__main__":
    main()