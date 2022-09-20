#Programming Assignment #3

from tkinter import S


def main():
    r1, r2 = [(1,1),(2,2),(3,3)], [(1,1),(1,2),(1,3),(1,4)]
    one = [one_a,one_b,one_c,one_d]
    for i in one:
        print(f"{i(r1,r2)}")

    r, s = [(1,1),(1,4),(2,3),(3,1),(3,4)], [(1,0),(2,0),(3,1),(3,2),(4,1)]
    print(f"{two(r,s)}")
    print(f"{three(r)}")

    #Insert Code for Question 4.

def union(rel1,rel2):
    result = []
    for x in rel1:
        for y in rel2:
            result.append(x)
            result.append(y)
    
    return f"{sorted(set(result))}"

def intersect(rel1,rel2):
    result = []
    for x in rel1:
        for y in rel2:
            if x == y:
                result.append(x)
    
    return f"{result}"

def diff(rel1,rel2):
    result = []
    for i in rel1:
        result.append(i)

    for x in rel1:
        for y in rel2:
            if x == y:
                result.remove(x)
    
    return f"{result}"

def compose(rel1,rel2):
    result = []
    for x in rel1:
        for y in rel2:
            if x[1] == y[0]:
                result.append((x[0],y[1]))

    return f"{result}"

def one_a(r1,r2):
    return f"1a.) R1 ∪ R2 = {union(r1,r2)}."

def one_b(r1,r2):
    return f"1b.) R1 ∩ R2 = {intersect(r1,r2)}."

def one_c(r1,r2):
    return f"1c.) R1 − R2 = {diff(r1,r2)}."

def one_d(r1,r2):
    return f"1d.) R2 − R1 = {diff(r2,r1)}."

def two(r,s):
    return f"2.)  S ◦ R = {compose(r,s)}."

def three(r):
    return f"3.) R^2 = {compose(r,r)}."

if __name__ == "__main__":
    main()