# Constants
SIZE = 6
NULL = -1

# Declaration of stack
stack = [None for i in range(SIZE)]

# Variables
top = NULL
free = SIZE

# Initialisation function
def initialise():
    global top
    for i in range(SIZE):
        stack[i] = None
    top = NULL
    free = SIZE

# Push operation
def push(data):
    global top, free
    if free > 0:
        top += 1
        stack[top] = data
        free -= 1
    else:
        print("Overflow error! Stack is full!")

# Pop operation
def pop():
    global top, free
    if free < SIZE:
        data = stack[top]
        top -= 1
        free += 1
        return data
    else:
        print("Underflow error! Stack is empty!")
        return False

# Display function
def display():
    for i in range(SIZE - 1, -1, -1):
        if i == top:
            print(i+1, ":", stack[i], "<-- Top")
        else:
            print(i+1, ":", stack[i])

# Main program; Command-line interface
while True:
    print("1. Initialise stack\n2. Push data\n3. Pop data\n4. Display stack\n5. Exit program")
    choice = input("Enter your choice:\n>>> ")

    if choice == '1':
        initialise()
    elif choice == '2':
        data = input("Enter data to be pushed:\n>>> ")
        push(data)
    elif choice == '3':
        data = pop()
        if data: # Print popped data if no errors occurred
            print("Popped data:", data)
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting program... ")
        break
    else:
        print("Invalid choice! Please choose carefully!")

    print()