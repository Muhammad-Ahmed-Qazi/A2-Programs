'''
# Algorithms
1. Linear search
2. Standard binary search
3. Recursive binary search
4. Insertion sort
5. Bubble sort
'''

array = [1, 5, 6, 78, 9, 15, 20, 35, 16, 17]
temp = sorted(array) # For binary search algorithm
LEN = len(array)


def linear_search(inp):
    flag = False; pos = 0

    for count in range(0, LEN):
        if array[count] == inp:
            flag = True
            pos = count
    
    return flag, pos

def binary_search(inp):
    # The array should be sorted for binary search algorithm to work
    temp = sorted(array)
    
    flag = False; pos = 0
    lower = 0; upper = LEN - 1

    while lower <= upper and flag == False:
        mid = (lower + upper) // 2
        if temp[mid] == inp:
            flag = True
            pos = mid
            print("FOUND!")
        elif temp[mid] < inp:
            lower = mid + 1
        elif temp[mid] > inp:
            upper = mid - 1
    
    return flag, pos

def recursive_binary_search(inp, lower, upper):
    mid = (lower + upper) // 2
    # Base case
    if lower > upper: return False

    # General cases
    if temp[mid] == inp:
        return mid
    elif temp[mid] < inp:
        return recursive_binary_search(inp, mid + 1, upper)
    elif temp[mid] > inp:
        return recursive_binary_search(inp, lower, mid - 1)

def insert_sort():
    master = slave = -1

    for master in range(1, LEN):
        key = array[master]
        slave = master - 1
        while slave >= 0 and key < array[slave]:
            array[slave + 1] = array[slave]
            slave -= 1
        array[slave + 1] = key


def bubble_sort():
    master = slave = 0
    swap = True

    while swap and master < LEN:
        swap = False
        master += 1
        for slave in range(1, LEN - 1):
            if array[slave - 1] > array[slave]:
                temp = array[slave]
                array[slave] = array[slave - 1]
                array[slave - 1] = temp
                swap = True
    

# Selection menu
while True:
    print("Select an algorithm to run on the following array of integers ", end = "")
    print(f"↓\n{array}\n")  # ASCII code for down arrow
    print("1. Linear search")
    print("2. Standard binary search")
    print("3. Recursive binary search")
    print("4. Insertion sort")
    print("5. Bubble sort")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        inp = int(input("Enter the element to search: "))
        flag, pos = linear_search(inp)
        if flag:
            print(f"Element {inp} found at position {pos}")
        else:
            print(f"Element {inp} not found")
    elif choice == 2:
        inp = int(input("Enter the element to search: "))
        flag, pos = binary_search(inp)
        if flag:
            print(f"Element {inp} found at position {pos}")
        else:
            print(f"Element {inp} not found")
    elif choice == 3:
        inp = int(input("Enter the element to search: "))
        pos = recursive_binary_search(inp, 0, LEN - 1)
        if pos is not False:
            print(f"Element {inp} found at position {pos}")
        else:
            print(f"Element {inp} not found")
    elif choice == 4:
        insert_sort()
        print("Insertion sort completed")
        print("Sorted array:", array)
    elif choice == 5:
        bubble_sort()
        print("Bubble sort completed")
        print("Sorted array:", array)

    elif choice == 0:
        break
    else:
        print("Invalid choice. Please try again.")