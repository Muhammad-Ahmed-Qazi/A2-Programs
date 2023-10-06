class student:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.level = ''

stack = [student() for i in range(6)]

null = -1
top = null

def initialise():
    global top, null

    for i in range(0, 6):
        stack[i] = student()
    
    top = null

def push(data):
    global top
    
    if top != (len(stack) - 1):
        top += 1
        ## Shorthand works!
        # stack[top] = data
        stack[top].id = data.id
        stack[top].name = data.name
        stack[top].level = data.level
        print("Data", "(", data.id, data.name, data.level, ")", "added at index", str(top), "of stack.\n")
    else:
        print("Overflow error! No space for additional data.\n")

def pop():
    global top
    data = student()

    if top != null:
        ## Shorthand works!
        # data = stack[top]
        data.id = stack[top].id
        data.name = stack[top].name
        data.level = stack[top].level
        top -= 1
        return data
    else:
        print("Underflow error! No elements remaining to pop.\n")

def display():
    for i in range(5, -1, -1):
        if i == top:
            print(stack[i].id, "|", stack[i].name, "|", stack[i].level, "|", "\t <-- top")
        else:
            print(stack[i].id, "|", stack[i].name, "|", stack[i].level)

while True:
    userInp = int(input("0: Initialise stack\n1: Push Data\n2: Pop Data\n3: Display stack\n4: Exit program\nSelect any operation: \n>>> "))
    if userInp == 0:
        initialise()
        print("Stack is initialised.\n")
    elif userInp == 1:
        data = student()
        print("Enter the set of data you want to push:")
        data.id = input("ID:\n>>>  ")
        data.name = input("Name:\n>>>  ")
        data.level = input("Level:\n>>>  ")
        push(data)
    elif userInp == 2:
        data = None
        data = pop()
        if data != None:
            print("Popped element is:", data.id, "|", data.name, "|", data.level, "\n")
    elif userInp == 3:
        display()
        print("\n")
    elif userInp == 4:
        print("Exiting program!")
        break