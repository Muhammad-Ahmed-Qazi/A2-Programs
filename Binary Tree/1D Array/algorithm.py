from colorama import Fore, Style, init
init()

ARR_SIZE = 10
NULL = -1

free = 0

lp = [None for i in range(ARR_SIZE)]
data = [None for i in range(ARR_SIZE)]
rp = [None for i in range(ARR_SIZE)]

def initBT():
    global free

    for i in range(ARR_SIZE):
        lp[i] = NULL
        rp[i] = NULL
        data[i] = None
    
    free = 0

def insert(val):
    global free
    prevNode = 0; currNode = 0;

    if free == 0:
        data[free] = val
        lp[free] = NULL
        rp[free] = NULL
        free += 1
        print(Fore.GREEN + "Value inserted!", Style.RESET_ALL)
    elif free == ARR_SIZE:
        print(Fore.RED + "Array is full!", Style.RESET_ALL)
    else:
        data[free] = val
        while currNode != NULL:
            prevNode = currNode
            if val < data[currNode]:
                currNode = lp[currNode]
            else:
                currNode = rp[currNode]
        if val < data[prevNode]:
            lp[prevNode] = free
        else:
            rp[prevNode] = free
        free += 1
        print(Fore.GREEN + "Value inserted!", Style.RESET_ALL)

def search(val):
    global free
    currNode = 0

    while currNode != NULL and val != data[currNode]:
        if val < data[currNode]:
            currNode = lp[currNode]
        else:
            currNode = rp[currNode]
    
    if currNode == NULL:
        print(Fore.RED + "Value not found!", Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Value found at", str(currNode) + "!", Style.RESET_ALL)

def display():
    for i in range(free):
        print("Node", str(i) + ":", end = " ")
        print("Data =", data[i], end = ", ")
        print("Left Pointer =", lp[i], end = ", ")
        print("Right Pointer =", rp[i])

def inOrder(node):
    if node != NULL:
        inOrder(lp[node])
        print(Fore.GREEN + str(data[node]), Style.RESET_ALL, end=" ")
        inOrder(rp[node])

def preOrder(node):
    if node != NULL:
        print(Fore.GREEN + str(data[node]), Style.RESET_ALL, end=" ")
        inOrder(lp[node])
        inOrder(rp[node])

def postOrder(node):
    if node != NULL:
        inOrder(lp[node])
        inOrder(rp[node])
        print(Fore.GREEN + str(data[node]), Style.RESET_ALL, end=" ")

# Main program
choice = 0
initBT()

while choice != 7:
    print(Fore.BLUE + "1. Insert", Style.RESET_ALL)
    print(Fore.BLUE + "2. Search", Style.RESET_ALL)
    print(Fore.BLUE + "3. Display", Style.RESET_ALL)
    print(Fore.BLUE + "4. Inorder Traversal", Style.RESET_ALL)
    print(Fore.BLUE + "5. Preorder Traversal", Style.RESET_ALL)
    print(Fore.BLUE + "6. Postorder Traversal", Style.RESET_ALL)
    print(Fore.BLUE + "7. Exit", Style.RESET_ALL)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to insert: "))
        insert(val)
    elif choice == 2:
        val = int(input("Enter value to search: "))
        search(val)
    elif choice == 3:
        display()
    elif choice == 4:
        inOrder(0)
        print("")
    elif choice == 5:
        preOrder(0)
        print("")
    elif choice == 6:
        postOrder(0)
        print("")
    elif choice == 7:
        print(Fore.CYAN + "Exiting...", Style.RESET_ALL)
    else:
        print(Fore.RED + "Invalid choice!", Style.RESET_ALL)