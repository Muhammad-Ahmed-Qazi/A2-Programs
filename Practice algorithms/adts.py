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
        self.head = -1

SIZE = 10

def initialise_arr(adt):
    if adt == 's' or adt == 'q':
        array = [None] * SIZE
    elif adt == 'b':
        array = [bin_tree()] * SIZE
    elif adt == 'l':
        array = [link_list()] * SIZE

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
    pass

class binary_tree():
    pass


# Main
    
my_stack = None
my_queue = None

while True:
    print("ADT Menu:")
    print("1. Stack")
    print("2. Queue")
    print("3. Exit")

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
                data = input("Enter the item to push: ")
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
                data = input("Enter the item to enqueue: ")
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
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
