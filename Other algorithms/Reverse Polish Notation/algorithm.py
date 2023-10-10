from colorama import Fore, Style, init
init()

import os, sys
print("Your current working directory is", os.getcwd())
curr = input("Enter the path to the folder containing the classes: ")
curr = os.path.join(str(os.getcwd()) + str(curr))
print(curr)
sys.path.insert(0, curr)

import stack as stClass

operators = {'+': 2, '-': 1, '*': 3, '/': 4}
brackets = ['(', ')']

userChoice = 0
postfix = None


def isHigherPrecedent(opCurr, opAgainst):
    if operators[opCurr] < operators[opAgainst] or operators[opCurr] == operators[opAgainst]:
        return True
    else:
        return False


def infixToPostfix(exp):
    exp = exp.replace(' ', '')
    for i in range(len(exp)):
        if i != len(exp) - 1:
            if exp[i] not in operators.keys() and exp[i] not in brackets and exp[i + 1] == '(':
                closeIndex = exp.find(')', i)
                exp = exp[:i] + '(' + exp[i] + '*' + exp[i + 1:closeIndex] + ')' + exp[closeIndex:]

    # print(exp)

    stack = stClass.MyStack(len(exp))
    result = ""

    i = 0
    while i < len(exp):
        curr = exp[i]
        try:
            if curr not in operators.keys() and curr != '(' and curr != ')' and curr != ' ':
                if exp[i + 1] != ' ' and exp[i + 1] not in operators.keys() and exp[i + 1] not in brackets:
                    curr += exp[i + 1]
                    i += 1
        except:
            pass

        if curr not in operators.keys() and curr not in brackets:
            result += curr + " "

        elif curr in operators.keys():
            popped = stack.pop()

            while popped != False and popped != '(' and isHigherPrecedent(curr, popped):
                result += popped + " " 
                popped = stack.pop()

            if popped in operators.keys() and not isHigherPrecedent(curr, popped):
                stack.push(popped)
            elif popped == '(':
                stack.push(popped)

            stack.push(curr)

        elif curr == '(':
            stack.push(curr)

        elif curr == ')':
            popped = stack.pop()

            while popped != False and popped != '(':
                result += popped + " "
                popped = stack.pop()

        # print(result)
        # stack.display()
        i += 1

    popped = stack.pop()

    while popped != False:
        result += popped + " "
        popped = stack.pop()
    
    return result

def evaluatePostfix(exp):
    i = 0
    stack = stClass.MyStack(len(exp))

    while i < len(exp):
        curr = exp[i]
        try:
            if curr not in operators.keys() and curr != '(' and curr != ')' and curr != ' ':
                if exp[i + 1] != ' ' and exp[i + 1] not in operators.keys() and exp[i + 1] not in brackets:
                    curr += exp[i + 1]
                    i += 1
        except:
            pass
        
        if curr not in operators.keys() and curr != ' ':
            stack.push(curr)
        elif curr != ' ':            
            try:
                b = float(stack.pop())
                a = float(stack.pop())

                if curr == '+': result = a + b
                elif curr == '-': result = a - b
                elif curr == '*': result = a * b
                elif curr == '/': result = a / b
            except:
                print(Fore.RED + "Expression is undecided! It cannot be solved!", Style.RESET_ALL)
                break
            
            try:
                result = str(float(result))
            except:
                result = str(result)
            
            stack.push(result)
            
        i += 1
    
    return stack.pop()

while userChoice != 3:
    print(Fore.BLUE + "1. Convert infix expression to postfix expression", Style.RESET_ALL)
    print(Fore.BLUE + "2. Evaluate postfix expression", Style.RESET_ALL)
    print(Fore.BLUE + "3. Exit", Style.RESET_ALL)
    userChoice = int(input("Enter your choice: "))

    if userChoice == 1:
        exp = input("Enter the infix expression: ")
        postfix = infixToPostfix(exp)
        print(Fore.GREEN + "Postfix expression:", postfix, Style.RESET_ALL)
    elif userChoice == 2:
        if postfix != None:
            userCalculated = input("Do you want the above converted infix expression to be evaluated? (y/N)\n>>> ")
            if userCalculated == 'y': print(Fore.GREEN + "Postfix expression:", evaluatePostfix(postfix), Style.RESET_ALL)
            elif userCalculated == 'N': 
                exp = input("Enter the postfix expression: ")
                print(Fore.GREEN + "Postfix expression:", evaluatePostfix(exp), Style.RESET_ALL)
        else:
            exp = input("Enter the postfix expression: ")
            print(Fore.GREEN + "Postfix expression:", evaluatePostfix(exp), Style.RESET_ALL)
    elif userChoice == 3:
        print(Fore.CYAN + "Thank you for using the program!", Style.RESET_ALL)
    else:
        print(Fore.RED + "Invalid choice! Try again.\n", Style.RESET_ALL)

    print("")
