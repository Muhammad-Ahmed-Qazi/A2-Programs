import os, sys
print("Your current working directory is", os.getcwd())
curr = input("Enter the path to the folder containing the classes: ")
print(os.path.join(str(os.getcwd()) + str(curr)))
curr = os.path.join(str(os.getcwd()) + str(curr)) # Path to classes folder
sys.path.insert(0, curr)
import stack as stClass # Importing stack class

operators = {'+': 2, '-': 1, '*': 3, '/': 4} # Dictionary of operators and their precedence according to BODMAS
brackets = ['(', ')']

userChoice = 0

# Function to check if the current operator has higher precedence than the operator at the top of the stack
def isHigherPrecedent(opCurr, opAgainst):
    if operators[opCurr] < operators[opAgainst] or operators[opCurr] == operators[opAgainst]:
        return True
    else:
        return False

# Function to convert infix expression to postfix expression
def infixToPostfix(exp):
    stack = stClass.MyStack(len(exp)) # Creating a stack object
    result = "" # String to store the postfix expression

    # Iterating through the expression
    for i in range(len(exp)):
        curr = exp[i]

        # Current character is an operand
        if curr not in operators.keys() and curr not in brackets:
            result += curr + " "

        # Current character is an operator
        elif curr in operators.keys():
            popped = stack.pop()

            # If the stack is not empty and the operator at the top of the stack has higher precedence than the current operator
            while popped != False and popped != '(' and isHigherPrecedent(curr, popped):
                result += popped + " " # Add the operator at the top of the stack to the result string
                popped = stack.pop()

            if popped in operators.keys() and not isHigherPrecedent(curr, popped):
                stack.push(popped) # Push the operator back to the stack
            elif popped == '(':
                stack.push(popped) # Push the operator back to the stack

            stack.push(curr) # Push the current operator to the stack

        # Current character is an opening bracket
        elif curr == '(':
            stack.push(curr)

        # Current character is a closing bracket
        elif curr == ')':
            popped = stack.pop()

            # Pop all the operators from the stack until an opening bracket is encountered
            while popped != False and popped != '(':
                result += popped + " "
                popped = stack.pop()

        # print(result)
        # stack.display()

    popped = stack.pop()

    # Pop all the remaining operators from the stack
    while popped != False:
        result += popped + " "
        popped = stack.pop()
    
    return result

def evaluatePostfix(exp):
    stack = stClass.MyStack(len(exp))
    

while userChoice != 2:
    print("1. Convert infix expression to postfix expression")
    print("2. Exit")
    userChoice = int(input("Enter your choice: "))

    if userChoice == 1:
        exp = input("Enter the expression: ")
        print("Postfix expression:", infixToPostfix(exp))
    elif userChoice == 2:
        print("Thank you for using the program!")
    else:
        print("Invalid choice! Try again.\n")
