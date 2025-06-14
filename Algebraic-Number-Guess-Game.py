import random

program_number = random.randint(1,100) #This generates the program number the user is attempting to guess.

print("Welcome! your objective is to guess the random number by simplifying the algebraic expression")

user_number = int(input("First make your guess. (keep it below 101):\n"))

def range_check(n): #This function takes in the user number and ensures it's within range.
    usernumber = n
    while int(n) > 100:
        n = int(input("Guess again, your number was out of range: "))
    else:
        return n

user_number = range_check(user_number)

first_operation = int(input("what is your first operation? (enter the number)\n1. * \n2. /\n"))

def first_operation_check(n): #This function takes in the operation and ensures it's within range.
    firstop = n
    while int(n) > 2:
        n = int(input("select again, invalid input: "))
    else:
        return n  

first_operation = first_operation_check(first_operation)

second_operation = int(input("what is your second operation? (enter the number)\n1. + \n2. -\n"))

def second_operation_check(n): #This function takes in the operation and ensures it's within range.
    secondop = n
    while int(n) > 2:
        n = int(input("select again, invalid input: "))
    else:
        return n  

second_operation = second_operation_check(second_operation)

print("your number is:\n"+str(user_number) + "\nyour first operation is:\n"+ str(first_operation) + "\nyour second operation is\n"+str(second_operation))

def variable_generator(pn, un, fo): #generates the value of the x variable. This is used to create the "term_2" number
    programnum = pn
    usernum = un
    firstop = fo
    if fo == 1:
        x = pn/un
    elif fo == 2:
        x = pn*un
    return float(x)

variable = variable_generator(program_number, user_number, first_operation)

if variable == float(program_number)*user_number: #determines the "term_2" number.
    term_2 = variable - float(program_number)
elif variable == program_number/user_number:
    term_2 = float(program_number) - variable 

#print("this is the program number: " + str(program_number))
#print("the variable is: " + str(variable))

if first_operation == 1 and second_operation == 1: #generates the actual expression.
    expression = int(input("here is your algebra expression:(plug x back in and round your number for the answer)\n" + str(user_number) + "x=" + str(term_2) +"+x"))
elif first_operation == 1 and second_operation == 2:
    expression = int(input("here is your algebra expression:(plug x back in and round your number for the answer)\n" + str(user_number) + "x=" + str(term_2 + (2*program_number)) + "-x"))
elif first_operation == 2 and second_operation == 1:
    expression = int(input("here is your algebra expression:(plug x back in and round your number for the answer)\n" + "x/" + str(user_number) + "=" + "x-" + str(term_2)))
elif first_operation == 2 and second_operation == 2:
    expression = int(input("here is your algebra expression:(plug x back in and round your number for the answer)\n" + "x/" + str(user_number) + "=" + str(term_2 + (2*program_number)) +"-x"))


def expression_check(exp, pn): # Checks if user answer matches the randomly generated program number
    if exp == pn:
        return "Well Done. You guessed the number correctly, you're a mathematical wizard!"
    else:
        return "Incorrect the answer is: " + str(pn)
    
print(expression_check(expression, program_number))
