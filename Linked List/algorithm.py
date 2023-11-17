# Constants
SIZE = 5
NULL = -1

# Definition of Node class/data type
class Node():
    def __init__(self):
        self.data = None
        self.next = NULL

# Linked list declaration
linkedList = [Node() for i in range(SIZE)]

# Variables
head = NULL
tail = NULL
free = 0

# Initialisation function
def initialisation():
    global head, tail, free
    head = NULL; tail = NULL; free = 0

    for i in range(SIZE):
        linkedList[i].data = None
        linkedList[i].next = i + 1
    
    linkedList[SIZE - 1].next = NULL

# Insertion function
def insert(data):
    global head, tail, free
    newNode = 0

    if free != NULL: # If linked list is full
        newNode = free
        linkedList[newNode].data = data
        free = linkedList[newNode].next
        if head == NULL: # If linked list is empty
            head = newNode
            tail = newNode
            linkedList[head].next = NULL
        elif data < linkedList[head].data: # If data entered is smaller than value at the head of linked list
            linkedList[newNode].next = head
            head = newNode
        print("Data inserted!")
    else:
        print("Overflow error! Data cannot be inserted!")

def display():
    print("Data:")
    curr = head
    while curr != NULL:
        print(linkedList[curr].data, end=" ")
        curr = linkedList[curr].next

while True:
    print("1. Initialise Linked List\n2. Insert data\n3. Display Linked List\n4. End program")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        initialisation()
    elif choice == 2:
        data = int(input("Enter the data: "))
        insert(data)
    elif choice == 3:
        display()
    elif choice == 4:
        print("Program ending...!")
        break
    else:
        print("Invalid choice! Please try again.")
    print("\n")