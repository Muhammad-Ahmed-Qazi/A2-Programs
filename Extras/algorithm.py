class linkedList():
    def __init__(self):
        self.data = None
        self.next = 0

list1 = [linkedList() for i in range(5)]

head = -1
tail = -1
free = 0

def initialise():
    global head, tail, free
    head = -1; tail = -1; free = 0

    for i in range(len(list1)):
        list1[i].data = 0
        list1[i].next = i + 1
    
    list1[len(list1) - 1].next = -1

def insert(val):
    global head, tail, free

    if free == -1:
        print("Overflow error! No more space!")
    else:
        newN = free
        free = list1[newN].next
        list1[newN].data = val
        if head == -1: # list is empty
            print("Cond 1!")
            head = newN
            tail = newN
            list1[head].next = -1
        elif val < list1[head].data: # value is smaller than head.data
            print("Cond 2!")
            list1[newN].next = head
            head = newN
        elif val > list1[tail].data: # value is greater than tail.data
            print("Cond 3!")
            list1[tail].next = newN
            tail = newN
            list1[newN].next = -1
        else: # value to be inserted in the middle of the list
            print("Cond 4!")
            prev = head
            curr = head
            while list1[curr].data < val:
                prev = curr
                curr = list1[curr].next
            
            list1[prev].next = newN
            list1[newN].next = curr
        print("tail:", tail, "head:", head, "free:", free, "newN:", newN)
        print("Data entered!")

# def display():
#     for i in range(len(list1)):
#         print(i, "|", list1[i].data, "|", list1[i].next)
# MASLA HAI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def display():
    global head
    i = head
    while list1[i].next != -1:
        print(list1[i].data)
        i = list1[i].next

initialise()

while True:
    print("1. Insert data\n2. Display list\n3. End program")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        userInp = int(input("Enter data: "))
        insert(userInp)
    elif choice == 2:
        display()
    elif choice == 3:
        print("Program ends!")
        break