'''
SoloLearn Code Challenge - Linear Equation 

Linear Equation can be written as:

eq_user = 'ax -b = c'
eq_user = 'c = -ax -b'
eq_user = 'c = -b -ax'

eq_user = 'ax = c'
eq_user = 'c = ax'

problem to solve is to predict all user inputs.

'''
import re

eq_user = input('Please enter Linear Equation: ')


def linear_eq(eq_user):
    # remove spaces from user input
    eq_user = re.sub(r' ', '', eq_user.lower())

    # extract digits using regular expression 
    eq_list = re.findall(r'-?\d+', eq_user)

    # searching for 'ax' value
    eq_a = re.findall(r'-?\d*x', eq_user)
    eq_a = re.findall(r'-?\d', eq_a[0])

    # checks if equation is written as 'ax = c', if True then b = 0, 
    if len(eq_list) == 2:
        eq_list.insert(1, '0')

        # Depends on the user input we can get lists:
    # eq = [a, b, c]
    # eq = [c, a, b]
    # eq = [c, b, a]
    # the task of the code below is to compare where in equations is 'ax' and sort result 
    # to get eq = [a, b, c] everytime.

    if eq_a[0] == eq_list[1]:
        eq_list.append(eq.pop(0))
    elif eq_a[0] == eq_list[2]:
        eq_list.append(eq_list.pop(2))
        eq_list = eq_list[::-1]

    # calculations

    a = float(eq_list[0])
    b = float(eq_list[1])
    c = float(eq_list[2])

    x = round((c - b) / a, 4)

    return (x)


x = linear_eq(eq_user)
print(f'Result of equation {eq_user} is {x}')
