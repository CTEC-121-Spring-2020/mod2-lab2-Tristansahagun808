"""
CTEC 121
<Tristan Sahagun>
<Mod2 Lab2>
<assignment/lab description>
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

import math
def main(): 
    '''
    mystring = "Hello"
    print(mystring)
    print(type(mystring))
    myInt = 33
    print(myInt)
    print(type(myInt))

    r=3
    v = (4/3)*pi*r**3
    print("v:", v)

    # Get a string
    aString = input("Enter a string of characters: ")
    print(aString)

    # Print 2 blank lines
    # print("\n\n")

    # Get an integer
    # int() does not accept decimals or non-numeric strings
    myInt = int(input("Enter a number: "))
    print(myInt)

    # Print 2 blank lines
    # print("\n\n")

    # Get a floating point number
    myFloat = float(input("Enter a number (decimals are ok): "))
    print(myFloat)

    # Print 2 blank lines
    # print("\n\n")

    # Evaluate an expression entered
    # Enter 3+4
    aNumber = eval(input("Enter a number or a numeric expressions: "))
    print(aNumber)

    # Print 2 blank lines
    # print("\n\n")
    
def main():
    print()

sum, diff = 3+2, 3-2
print(sum, diff)
print()

x, y = eval(input("Enter two numbers separated by a comma: "))
print(x, y)
print(type(x))
print()

x, y = input("provide two values: ").split()
print(x, y)
print(type(x))
x= int(x)
print(type(x))
print()

    #demo definite loops
    for i in [10, 1, 2, 3]:
        print (i)
    print()

    for count in range(4):
        print(count)
    print()

    for i in range(2,11,2):
        print(i)
        
    # math library use
    print(math.pi)
    print(math.sqrt(4))
    print(math.ceil(math.pi))
    print(math.floor(math.pi))

    sum = 0
    for i in [56, 19, 92, 67]:
        print(i)
        sum = sum + i
    print("------")
    print(sum)
    '''

    # get input and accumulate a sum
    sum = 0
    for i in range(5):
        inputvalue = eval(input("Enter a number: "))
        sum = sum + inputvalue
    print("sum:", sum)
    print()

main()