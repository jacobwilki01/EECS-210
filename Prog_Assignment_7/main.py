from math import *

def partition(n,k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif k == 0:
        return 0
    else:
        return partition(n-k,k) + partition(n,k-1)

def sterling2(n,k):
    if n == 0:
        return 0
    if k == 0:
        return 0
    if n == k:
        return 1
    if k > n:
        return 0
    else:
        return k * sterling2(n-1,k) + sterling2(n-1,k-1)

def combination(n,r):
    return factorial(n) / (factorial(r) * factorial(n-r))

def dist_dist(objects,boxes,per_box):
    box = []
    for _ in range(boxes):
        box.append(per_box)

    temp = 0
    denom = 1
    for i in range(len(box)):
        temp += box[i]
        box[i] = factorial(box[i])
        denom *= box[i]

    if temp != objects:
        denom *= factorial(objects-temp)

    return factorial(objects) / denom

def indist_dist(objects,boxes):
    return combination(objects+boxes-1,boxes-1)

def dist_indist(objects,boxes):
    return sterling2(objects,boxes) + sterling2(objects,boxes-1) + 1

def indist_indist(objects,boxes):
    return partition(objects,boxes)

def main():
    print("1.) There are",dist_dist(52,4,5),"ways to distribute 40 objects into 4 boxes with 10 objects in each box.")
    print("2.) There are", indist_dist(12,6), "ways to distribute 12 indistinguishable objects into 6 distinguishable boxes")
    print("3.) There are", dist_indist(5,4), "ways to distribute 5 distinguishable objects into 4 indistinguishable boxes")
    print("4.) There are", indist_indist(5,3),"ways to distribute 5 indistinguishable objects into 3 indistinguishable boxes")

if __name__ == "__main__":
    main()