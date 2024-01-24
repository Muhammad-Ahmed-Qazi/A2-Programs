'''
# Abstract Data Types (ADTs)
1. Stack
2. Queue
3. Linked List
4. Binary Tree
'''

class bin_tree():
    def __init__(self) -> None:
        self.left = -1
        self.data = None
        self.right = -1

class link_list():
    def __init__(self) -> None:
        self.data = None
        self.next = -1

SIZE = 10

def initialise_arr(adt):
    if adt == 's' or adt == 'q':
        array = [None] * SIZE
    elif adt == 'b':
        array = [bin_tree()] * SIZE
    elif adt == 'l':
        # array = [link_list()] * SIZE # This thing doesn't work because it creates a single object and copies its reference to all the elements of the array
        array = [link_list() for i in range(SIZE)]
        for i in range(0, SIZE):
            array[i].next = i + 1
        array[SIZE - 1].next = -1

    return array

class stack():
    def __init__(self) -> None:
        self.array = initialise_arr('s')
        self.pointer = -1
    
    def push(self, data):
        if self.pointer != SIZE - 1:
            self.pointer += 1
            self.array[self.pointer] = data
        else:
            return "Stack is full! No more insertions possible!"

        return "Insertion successful! Item added to the stack!"

    def pop(self):
        if self.pointer != -1:
            data =  self.array[self.pointer]
            self.pointer -= 1
        else:
            return "Stack is empty! No more deletion possible!", -1
        
        return "Deletion successful! Here's the item popped:", data

    def display(self):
        string = ""

        for pointer in range(SIZE - 1, -1, -1):
            if pointer != self.pointer:
                string = string + str(self.array[pointer]) + ", "
            else:
                string = string + str(self.array[pointer]) + "*, "
        
        return string[:-2]

class queue():
    def __init__(self) -> None:
        self.array = initialise_arr('q')
        self.front = -1
        self.rear = -1
        self.size = 0
    
    def enqueue(self, data):
        if self.size != SIZE:
            if self.size == 0:
                self.front = 0
                self.rear = 0
            else:
                self.rear = (self.rear + 1) % SIZE
            self.array[self.rear] = data
            self.size += 1
        else:
            return "Queue is full! No more insertions possible!"

        return "Insertion successful! Item added to the queue!"
    
    def dequeue(self):
        if self.size != 0:
            data = self.array[self.front]
            self.front = (self.front + 1) % SIZE
            self.size -= 1
        else:
            return "Queue is empty! No more deletion possible!", -1
        
        return "Deletion successful! Here's the item dequeued:", data

    def display(self):
        string = ""

        for pointer in range(SIZE - 1, -1, -1):
            if pointer != self.front and pointer != self.rear:
                string = string + str(self.array[pointer]) + ", "
            elif pointer == self.front:
                string = string + str(self.array[pointer]) + "*, "
            elif pointer == self.rear:
                string = string + str(self.array[pointer]) + "!, "
            
        return string[:-2]

class linked_list():
    def __init__(self) -> None:
        self.array = initialise_arr('l')
        self.head = -1
        self.tail = -1
        self.free = 0
    
    def insert(self, data):
        newNode = 0
        print(self.array[self.head].data, data)
        # print(data < self.array[self.head].data)

        if self.free != -1:
            newNode = self.free
            self.array[newNode].data = data
            self.free = self.array[newNode].next
            if self.head == -1:
                print("Linked list was empty!")
                self.head = newNode
                self.tail = newNode
                self.array[self.head].next = -1
            elif data < self.array[self.head].data:
                print("Data is smaller than the head!")
                self.array[newNode].next = self.head
                self.head = newNode
            elif data > self.array[self.tail].data:
                print("Data is larger than the tail!")
                self.array[self.tail].next = newNode
                self.array[newNode].next = -1
                self.tail = newNode
            else:
                print("Data is somewhere in the middle!")
                curr = self.head
                while data > self.array[self.array[curr].next].data:
                    curr = self.array[curr].next
                self.array[newNode].next = self.array[curr].next
                self.array[curr].next = newNode
            print("Head:", self.head, "Tail:", self.tail)
        else:
            return "Overflow error! Data cannot be inserted!"

        return "Insertion successful! Item added to the linked list!"
    
    def search(self, data):
        curr = self.head
        
        while curr != -1:
            if self.array[curr].data == data:
                return "Data found! Here's the position:", curr
            curr = self.array[curr].next
        
        return "Data not found!", -1

    def delete(self, data):
        position = self.search(data)[1]
        
        if position != -1:
            if position == self.head:
                self.head = self.array[self.head].next
            else:
                curr = self.head
                while self.array[curr].next != position:
                    curr = self.array[curr].next
                self.array[curr].next = self.array[position].next
                if position == self.tail:
                    self.tail = curr
            self.array[position].next = self.free
            self.free = position
        else:
            return "Item to be deleted was not found!"
    
        return "Deletion successful! Item deleted from the linked list!"
    
    def display(self):
        string = ""
        curr = self.head

        while curr != -1:
            string = string + str(self.array[curr].data) + ", "
            curr = self.array[curr].next
        
        return string[:-2]


class binary_tree():
    pass


# Main
    
my_stack = None
my_queue = None
my_linked_list = None

while True:
    print("ADT Menu:")
    print("1. Stack")
    print("2. Queue")
    print("3. Linked List")
    print("4. Exit")

    adt_choice = int(input("Enter your choice for ADT: "))

    if adt_choice == 1:
        my_stack = stack()
        while True:
            print("Stack Menu:")
            print("1. Push")
            print("2. Pop")
            print("3. Display")
            print("4. Back to ADT Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                data = int(input("Enter the item to push: "))
                result = my_stack.push(data)
                print(result)
            elif choice == 2:
                result, data = my_stack.pop()
                print(result, data)
            elif choice == 3:
                print("* indicates position of the pointer.")
                result = my_stack.display()
                print(result)
            elif choice == 4:
                print("Going back to ADT Menu...")
                break
            else:
                print("Invalid choice! Please try again.")

    elif adt_choice == 2:
        my_queue = queue()
        while True:
            print("Queue Menu:")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Display")
            print("4. Back to ADT Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                data = int(input("Enter the item to enqueue: "))
                result = my_queue.enqueue(data)
                print(result)
            elif choice == 2:
                result, data = my_queue.dequeue()
                print(result, data)
            elif choice == 3:
                print("* indicates position of the front pointer.\n! indicates position of the rear.")
                result = my_queue.display()
                print(result)
            elif choice == 4:
                print("Going back to ADT Menu...")
                break
            else:
                print("Invalid choice! Please try again.")

    elif adt_choice == 3:
        my_linked_list = linked_list()
        while True:
            print("Linked List Menu:")
            print("1. Insert")
            print("2. Search")
            print("3. Delete")
            print("4. Display")
            print("5. Back to ADT Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                data = int(input("Enter the item to insert: "))
                result = my_linked_list.insert(data)
                print(result)
            elif choice == 2:
                data = int(input("Enter the item to search: "))
                result, data = my_linked_list.search(data)
                print(result, data)
            elif choice == 3:
                data = int(input("Enter the item to delete: "))
                result = my_linked_list.delete(data)
                print(result)
            elif choice == 4:
                result = my_linked_list.display()
                print(result)
            elif choice == 5:
                print("Going back to ADT Menu...")
                break
            else:
                print("Invalid choice! Please try again.")

    elif adt_choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
