def main():
    r1, s1 = [(1,1),(4,4),(2,2),(3,3)], [1,2,3,4]
    r2, s2 = [('a','a'),('c','c')], ['a','b','c','d']

    print(one(r1,s1)) #one_d
    print(one(r2,s2)) #one_e

    r3, r4 = [(1,2), (4,4), (2,1), (3,3)], [(1,2), (3,3)]

    print(two(r3)) #two_d
    print(two(r4)) #two_e

    r5, r6 = [('a','b'), ('d','d'), ('b','c'), ('a','c')], [(1,1),(1,3),(2,2),(3,1),(3,2)]

    print(three(r5)) #three_d
    print(three(r6)) #three_e

    r7, s3 = [(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)], [1, 2, 3, 4]
    r8, s4 = [(0, 0), (0, 1), (0, 2), (0, 3), (1,0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)], [0, 1, 2, 3]

    print(four(r7,s3)) #four_d
    print(four(r8,s4)) #four_e

    print(five(r7,s3)) #five_e
    print(five(r8,s4)) #five_f

#take in relation, set; return boolean
def reflexive(relation,set):
    for value in set:
        check = False
        for pair in relation:
            if pair == (value,value):
                check = True
        if not check:
            break
    
    return check

def symmetric(relation):
    for x in relation:
        check = False
        for y in relation:
            if y == (x[1],x[0]):
                check = True
        if not check:
            break

    return check

def antisymmetric(relation):
    if not symmetric(relation):
        for x in relation:
            check = True
            for y in relation:
                if y == (x[1],x[0]) and x[0] != x[1]:
                    check = False
            if not check:
                break

        return check
    else:
        return False

def transitive(relation):
    temp = []
    for pair in relation:
        if pair[0] != pair[1]:
            temp.append(pair)
    
    for x in temp:
        check = False
        for y in temp:
            if x[1] == y[0]:
                for z in temp:
                    if z == (x[0],y[1]):
                        check = True
                        temp.remove(x)
                        temp.remove(y)
                        temp.remove(z)
        if not check:
            break

    return check

#takes in a relation; returns a string it with {} instead of []
def print_rel(relation):
    result = "{"
    for x in range(0,len(relation)):
        if x != len(relation) - 1:
            result += f"{relation[x]}, "
        else:
            result += f"{relation[x]}"

    return result + "}"

#takes in a set, relation; returns closure
def rel_close(set,relation):
    closure = relation
    for value in set:
        check = False
        for pair in relation:
            if pair == (value,value):
                check = True
        if not check:
            closure.append((value,value))
    
    return closure

def symm_close(relation):
    closure = relation
    for x in relation:
        check = False
        for y in relation:
            if y == (x[1],x[0]):
                check = True
        if not check:
            closure.append((x[1],x[0]))

    return closure

def trans_close(relation):
    temp, removed = [], []
    for pair in relation:
        if pair[0] != pair[1]:
            temp.append(pair)
        else:
            removed.append(pair)
    
    for x in temp:
        check = False
        for y in temp:
            if x[1] == y[0]:
                for z in temp:
                    if z != (x[0],y[1]) and x != z and y != z:
                        temp.append((x[0],y[1]))
                        check = True
                        break
        if check:
            break
    
    for item in removed:
        temp.append(item)
    
    return sorted(set(temp))
    
def one(relation,set):
    if reflexive(relation,set):
        return f"1a.) R = {print_rel(relation)}.\n1b.) R is reflexive.\n"
    else:
        return f"1a.) R = {print_rel(relation)}.\n1b.) R is not reflexive.\n1c.) R* = {print_rel(rel_close(set,relation))}.\n"

def two(relation):
    if symmetric(relation):
        return f"2a.) R = {print_rel(relation)}.\n2b.) R is symmetric.\n"
    else:
        return f"2a.) R = {print_rel(relation)}.\n2b.) R is not symmetric.\n2c.) R* = {print_rel(symm_close(relation))}.\n"

def three(relation):
    if transitive(relation):
        return f"3a.) R = {print_rel(relation)}.\n3b.) R is transitive.\n"
    else:
        return f"3a.) R = {print_rel(relation)}.\n3b.) R is not transitive.\n3c.) R* = {print_rel(trans_close(relation))}.\n"

def four(relation, set):
    reflex, symm, trans = reflexive(relation, set), symmetric(relation), transitive(relation)
    if reflex and symm and trans:
        return f"4a.) R = {print_rel(relation)}.\n4b.) R is an equivalence relation.\n"
    else:
        string = f"4a.) R = {print_rel(relation)}.\n4b.) R is not an equivalence relation.\n4c.) R is not an equivalence relation because it is "
        
        if not reflex:
            if not symm:
                if not trans:
                    string += f"not reflexive, symmetric, and transitive.\n"
                else:
                    string += f"not reflexive and symmetric.\n"
            else:
                if not trans:
                    string += f"not reflexive and transitve.\n"
                else:
                    string += f"not reflexive.\n"
        elif not symm:
            if not trans:
                string += f"not symmetric and transitive.\n"
            else:
                string += f"not symmetric.\n"
        else:
            string += f"not transitive.\n"

        return string

def five(relation,set):
    reflex, antisymm, trans = reflexive(relation,set), antisymmetric(relation), transitive(relation)
    if reflex and antisymm and trans:
        return f"5a.) S = {print_rel(set)}.\n5b.) R = {print_rel(relation)}.\n5c.) (S,R) is a poset.\n"
    else:
        string = f"5a.) S = {print_rel(set)}.\n5b.) R = {print_rel(relation)}.\n5c.) (S,R) is not a poset because it is "
        
        if not reflex:
            if not antisymm:
                if not trans:
                    string += f"not reflexive, antisymmetric, and transitive.\n"
                else:
                    string += f"not reflexive and antisymmetric.\n"
            else:
                if not trans:
                    string += f"not reflexive and transitve.\n"
                else:
                    string += f"not reflexive.\n"
        elif not antisymm:
            if not trans:
                string += f"not antisymmetric and transitive.\n"
            else:
                string += f"not antisymmetric.\n"
        else:
            string += f"not transitive.\n"

        return string

if __name__ == "__main__":
    main()