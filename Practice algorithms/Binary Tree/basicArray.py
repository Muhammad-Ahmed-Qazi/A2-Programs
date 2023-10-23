# Constants
SIZE = 10
NULL = -1

# Declaration
lp = [NULL for i in range(SIZE)]
data = [None for i in range(SIZE)]
rp = [NULL for i in range(SIZE)]

# Variables
index = 0
free = SIZE

# Initialisation function
def initialise():
    global index, free
    for i in range(SIZE):
        lp[i] = NULL
        data[i] = None
        rp[i] = NULL
    index = 0
    free = SIZE

# Creating nodes
def newNode(index, currNode, right):
    if right == True:
        rp[currNode] = index
    else:
        lp[currNode] = index

# Insert operation
def insert(val):
    global index, free
    # Local variables
    prevNode = 0
    currNode = 0
    
    if free == SIZE:
        data[index] = val
        index += 1
        free -= 1
    elif free < SIZE and free > 0:
        data[index] = val
        while currNode != NULL:
            prevNode = currNode
            if data[prevNode] < val:
                currNode = rp[prevNode]
                if currNode == NULL: newNode(index, prevNode, True)
            elif data[prevNode] > val:
                currNode = lp[prevNode]
                if currNode == NULL: newNode(index, prevNode, False)
        index += 1
        free -= 1
    else:
        print("Overflow error! Array is full!")

# Search operation
def search(val):
    # Local variable
    currNode = 0
    
    while currNode != NULL:
        if data[currNode] == val:
            return currNode
        elif data[currNode] < val:
            currNode = rp[currNode]
        elif data[currNode] > val:
            currNode = lp[currNode]
    return False

# Inorder traversal operation
def inorder(node):
    if node != NULL:
        inorder(lp[node])
        print(data[node], end=" ")
        inorder(rp[node])

# Preorder traversal operation
def preorder(node):
    if node != NULL:
        print(data[node], end=" ")
        preorder(lp[node])
        preorder(rp[node])

# Postorder traversal operation
def postorder(node):
    if node != NULL:
        postorder(lp[node])
        postorder(rp[node])
        print(data[node], end=" ")

# Display function
def display():
    for i in range(SIZE):
        print(i, ":", lp[i], data[i], rp[i])
    
# Main program; Command-line interface
while True:
    print("1. Initialise Binary Tree\n2. Insert data\n3. Search for data\n4. Inorder traversal\n5. Preorder traversal\n6. Postorder traversal\n7. Display queue\n8. Exit program")
    choice = input("Enter your choice:\n>>> ")

    if choice == '1':
        initialise()
    elif choice == '2':
        userInp = int(input("Enter data to be inserted:\n>>> "))
        insert(userInp)
    elif choice == '3':
        userInp = int(input("Enter data to be searched:\n>>> "))
        result = search(userInp)
        if result: print("Value found at", str(result) + "!")
        else: print("Value not found!")
    elif choice == '4':
        inorder(0); print()
    elif choice == '5':
        preorder(0); print()
    elif choice =='6':
        postorder(0); print()
    elif choice == '7':
        display()
    elif choice == '8':
        print("Exiting program... ")
        break
    else:
        print("Invalid choice! Please choose carefully!")
    print()
