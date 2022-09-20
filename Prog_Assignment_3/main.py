#Programming Assignment #3

from tkinter import S


def main():
    questions = [one(),two(),three(),four()]
    for question in questions:
        question

def union(rel1,rel2):
    result = []
    for x in rel1:
        for y in rel2:
            result.append(x)
    
    return f"R1 ∪ R2 = {sorted(set(result))}"

def intersect(rel1,rel2):
    result = []
    for x in rel1:
        for y in rel2:
            if x == y:
                result.append(x)
    
    return f"R1 ∩ R2 = {result}"

def diff(rel1,rel2):
    result = []
    for i in rel1:
        result.append(i)

    for x in rel1:
        for y in rel2:
            if x == y:
                result.remove(x)
    
    return f"R1 − R2 = {result}"

def compose(rel1,rel2):
    result = []
    for x in rel1:
        for y in rel2:
            if x[1] == y[0]:
                result.append((x[0],y[1]))

    return f"{result}"

def one():
    r1, r2 = [(1,1),(2,2),(3,3)], [(1,1),(1,2),(1,3),(1,4)]
    mode, letter = [union,intersect,diff], ['a','b','c']
    for x in range(0,len(letter)):
        print(f"1{letter[x]}.) {mode[x](r1,r2)}.")
    
    print(f"1d.) {diff(r2,r1)}")

def two():
    r, s = [(1,1),(1,4),(2,3),(3,1),(3,4)], [(1,0),(2,0),(3,1),(3,2),(4,1)]

    print(f"2.) S ◦ R = {compose(r,s)}")

def three():
    r = [(1,1),(1,4),(2,3),(3,1),(3,4)]

    print(f"3.) R^2 = {compose(r,r)}")

def four():
    pass

if __name__ == "__main__":
    main()