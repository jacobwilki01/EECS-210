'''
Code Name: EECs 210 - Programming Assignment 7
Description: This program will calculate the number of ways to distribute objects into boxes

Author: Jacob Wilkus
Date Created: November 16th, 2022

Preconditions and Postconditions:
    -partition(n,k):
        -Precondition: n and k are integers
        -Postcondition: returns the number of ways to partition n objects into k groupings
    -sterling2(n,k):
        -Precondition: n and k are integers
        -Postcondition: returns the number of ways to partition n objects into k groupings
    -combination(n,r):
        -Precondition: n and r are integers
        -Postcondition: returns the number of ways to choose r objects from n objects
    -dist_dist(objects,boxes,per_box):
        -Precondition: objects, boxes, and per_box are integers
        -Postcondition: returns the number of ways to distribute objects into boxes
    -indist_dist(objects,boxes):
        -Precondition: objects and boxes are integers
        -Postcondition: returns the number of ways to distribute objects into boxes
    -dist_indist(objects,boxes):
        -Precondition: objects and boxes are integers
        -Postcondition: returns the number of ways to distribute objects into boxes
    -indist_indist(objects,boxes):
        -Precondition: objects and boxes are integers
        -Postcondition: returns the number of ways to distribute objects into boxes
    -main():
        -Precondition: None
        -Postcondition: prints the number of ways to distribute objects into boxes
'''

from math import * #imports relevant functions from python's math module

#Partition function
def partition(n,k):
    if n == 0: #if n is 0, return 1
        return 1
    elif n < 0: #if n is less than 0, return 0
        return 0
    elif k == 0: #if k is 0, return 0
        return 0
    else: #if none of the above conditions are met, return the sum of the partition function with n and k-1 and the partition function with n-k and k
        return partition(n-k,k) + partition(n,k-1)

#Sterling2 Function
def sterling2(n,k):
    if n == 0: #if n is 0, return 0
        return 0
    if k == 0: #if k is 0, return 0
        return 0
    if n == k: #if n is equal to k, return 1
        return 1
    if k > n: #if k is greater than n, return 0
        return 0
    else: #if none of the above conditions are met, return the sum of the sterling2 function with n-1 and k-1 and the sterling2 function with n-1 and k
        return k * sterling2(n-1,k) + sterling2(n-1,k-1)

#Combination function. Returns the number of ways to choose r objects from n objects
def combination(n,r):
    return factorial(n) / (factorial(r) * factorial(n-r))

#Distinguishable Objects to Distinguishable Boxes Distribution Function
def dist_dist(objects,boxes,per_box):
    box = [] #creates an empty list
    for _ in range(boxes): #for loop that runs for the number of boxes
        box.append(per_box) #appends per_box to the list

    temp = 0 #creates a temporary variable
    denom = 1 #creates a denominator variable
    for i in range(len(box)): #for loop that runs for the length of the list
        temp += box[i] #adds the value of the list at index i to temp
        box[i] = factorial(box[i]) #sets the value of the list at index i to the factorial of the value of the list at index i
        denom *= box[i] #multiplies the value of the list at index i to the denominator variable

    if temp != objects: #if the value of temp is not equal to the number of objects, return 0
        denom *= factorial(objects-temp) #multiplies the factorial of the difference between the number of objects and temp to the denominator variable

    return factorial(objects) / denom #returns the factorial of the number of objects divided by the denominator variable

#Indistinguishable Objects to Distinguishable Boxes Distribution Function. Returns the number of ways to distribute objects into boxes using combination().
def indist_dist(objects,boxes):
    return combination(objects+boxes-1,boxes-1)

#Distinguishable Objects to Indistinguishable Boxes Distribution Function. Returns the number of ways to distribute objects into boxes using sterling2().
def dist_indist(objects,boxes):
    return sterling2(objects,boxes) + sterling2(objects,boxes-1) + 1

#Indistinguishable Objects to Indistinguishable Boxes Distribution Function. Returns the number of ways to distribute objects into boxes using partition().
def indist_indist(objects,boxes):
    return partition(objects,boxes)

#Main Function. Prints the results.
def main():
    print("1.) There are",dist_dist(52,4,5),"ways to distribute 40 objects into 4 boxes with 10 objects in each box.")
    print("2.) There are", indist_dist(12,6), "ways to distribute 12 indistinguishable objects into 6 distinguishable boxes")
    print("3.) There are", dist_indist(5,4), "ways to distribute 5 distinguishable objects into 4 indistinguishable boxes")
    print("4.) There are", indist_indist(5,3),"ways to distribute 5 indistinguishable objects into 3 indistinguishable boxes")

if __name__ == "__main__":
    main()