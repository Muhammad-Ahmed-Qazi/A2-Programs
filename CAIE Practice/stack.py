SIZE = 10
NULL = -1

stack = [None for i in range(SIZE)]

top = NULL

def initialise():
    global top

    for i in range(SIZE):
        stack[i] = None
    
    top = NULL

def push(data):
    global top

    if top != (len(stack) - 1):
        top += 1
        stack[top] = data
        print("Data stored!")
    else:
        print("Overflow error! Stack is full!")

def pop():
    global top

    if top != NULL:
        print("Data popped:", stack[top])
        top -= 1
    else:
        print("Underflow error! Stack is empty!")

initialise()
print(stack)
push(23)
print(stack)
pop()
pop()