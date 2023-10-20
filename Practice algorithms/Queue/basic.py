# Constants
SIZE = 6
NULL = -1

# Declaration
queue = [None for i in range(SIZE)]

# Variables
front = NULL
tail= NULL
free = SIZE

# Initialisation function
def initialise():
    global front, tail, free
    for i in range(SIZE):
        queue[i] = None
    front = NULL
    tail = NULL
    free = SIZE

# Enqueue operation
def enqueue(data):
    global front, tail, free
    if free > 0:
        if free == SIZE:
            front = 0
            tail += 1
            queue[tail] = data
            free -= 1
        elif free < SIZE:
            tail += 1
            if tail == SIZE:
                tail = 0
            queue[tail] = data
            free -= 1
    else:
        print("Overflow error! Queue is full!")

# Dequeue operation
def dequeue():
    global front, tail, free
    if free < SIZE:
        data = queue[front]
        front += 1
        if front == SIZE:
            front = 0
        free += 1
        return data
    else:
        print("Underflow error! Queue is empty!")
        return False

# Display function
def display():
    for i in range(SIZE):
        if i == front:
            print(i+1, ":", queue[i], "<-- Front")
        elif i == tail:
            print(i+1, ":", queue[i], "<-- Tail")
        else:
            print(i+1, ":", queue[i])

# Main program; Command-line interface
while True:
    print("1. Initialise queue\n2. Insert data\n3. Delete data\n4. Display queue\n5. Exit program")
    choice = input("Enter your choice:\n>>> ")

    if choice == '1':
        initialise()
    elif choice == '2':
        data = input("Enter data to be inserted:\n>>> ")
        enqueue(data)
    elif choice == '3':
        result = dequeue()
        if result: # Print deleted data if no errors occurred
            print("Deleted data:", result)
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting program... ")
        break
    else:
        print("Invalid choice! Please choose carefully!")

    print()
