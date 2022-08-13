'''
EECS 210 -- Programming Assignment #1
Author: Jacob Wilkus
KUID: 3020877
'''

#The main() function for the program. Handles the printing for identification, and calling upon table() for each equation
def main():
    #Calls the table() function for the 6 equations. The value of each equation is hardcoded to an integer in the order of the Assignment Worksheet. (So, De Morgan's First Law is 0, Second Law is 1, etc.)
    for x in range(0,6):
        table(function)

#The table() function. Passes through which equation it is outputting to the data() function, and then takes the results from data() to fill out the table.
def table(function):
    results = data(function)

#Takes in a function name, does math to determine the values for the truth table.
def data(function):
    #Basic variables needed to make the code function.
    results = []
    names = ["== De Morgan's First Law ==", "== De Morgan's Second Law ==", "== First Associative Law ==", "== Second Associative Law ==", "== [(p + q) * (p -> r) * (p -> r)] -> r = T ==", "== p <-> q = (p -> q) * (q -> p) =="]

if __name__ == "__main__":
    main()