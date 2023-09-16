stack = [None for i in range(6)]

null = -1
top = null

def initialise():
    global top, null

    for i in range(0, 6):
        stack[i] = None
    
    top = null

def push(data):
    global top
    
    if top != (len(stack) - 1):
        top += 1
        stack[top] = data
        print("Data", "(", data, ")", "added at index", str(top), "of stack.\n")
    else:
        print("Overflow error! No space for additional data.\n")

def pop():
    global top

    if top != null:
        data = stack[top]
        top -= 1
        return data
    else:
        print("Underflow error! No elements remaining to pop.\n")

def display():
    for i in range(5, -1, -1):
        if i == top:
            print(stack[i], "   <--- top")
        else:
            print(stack[i])

while True:
    userInp = int(input("0: Initialise stack\n1: Push Data\n2: Pop Data\n3: Display stack\n 4: Exit program\nSelect any operation: \n>>> "))
    if userInp == 0:
        initialise()
        print("Stack is initialised.\n")
    elif userInp == 1:
        data = input("Enter a character you want to push: ")
        push(data)
    elif userInp == 2:
        data = None
        data = pop()
        if data != None:
            print("Popped element is:", data, "\n")
    elif userInp == 3:
        display()
        print("\n")
    elif userInp == 4:
        print("Exiting program!")
        break