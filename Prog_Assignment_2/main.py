#Programming Assignment 2

def main():
    one = [one_a(),one_b(),one_c(),one_d(),one_e(),one_f()]
    for letter in one:
        print(letter)

    print("")

    two = [two_a(),two_b(),two_c(),two_d()]
    for letter in two:
        print(letter)

def universal(list):
    for value in list:
        if value == False:
            return False
    return True

def existential(list):
    for value in list:
        if value == True:
            return True
    return False

def disjunction(list1,list2):
    result = []
    for x in range(0,len(list1)):
        if not (list1[x] or list2[x]):
            result.append(False)
        else:
            result.append(True)
    
    return result

def conjunction(list1,list2):
    result = []
    for x in range(0,len(list1)):
        if not (list1[x] and list2[x]):
            result.append(False)
        else:
            result.append(True)
    
    return result

def negation(list):
    result = []
    for item in list:
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
            return f"x * y does not equal 0 when x is {return_x} and y is {return_y}"
        else:
            if mode_x == "univ":
                return f"x * y does not equal 0 when x is {return_x} and y is not 0"
            elif mode_y == "univ":
                return f"x * y does not equal 0 when y is {return_y} and x is not 0"

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
    
    return f"1d.) {universal(final)} because {proof_large('exis','or','less than 2','greater than 7',final)}."

def one_e():
    pass

def one_f():
    pass 

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