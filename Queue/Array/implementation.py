queue = [None for i in range(8)]

null = -1
front = null
rear = null

size = 0
capacity = len(queue)

def initialize():
    global front, rear, size
    front = rear = null
    size = 0

    for i in range(capacity):
        queue[i] = None

def enqueue(data):
    global front, rear, size
    
    if size == capacity:
        print("Queue is full!")
        return
    
    rear = (rear + 1) % capacity
    queue[rear] = data
    size += 1

def dequeue():
    global front, rear, size

    if size == 0:
        print("Queue is empty!")
        return

    front = (front + 1) % capacity
    size -= 1
    return queue[front]

def display():
    global front, rear
    # Check if queue is empty
    if front == -1 and rear == -1:
        print("Queue is empty\n")
    else:
        print("Elements in the queue: ")
        # Iterate through the elements in the queue and 
        # print them out in order
        i = front
        while i != rear:
            print(queue[i], end=" ")
            # i is incremented in a circular fashion
            i = (i + 1) % len(queue) 
        print(queue[rear], end=" ")
        print("\n")
        print("Front:", front)
        print("Rear:", rear)
        # Print the size of the queue by subtracting the front
        # pointer from the rear pointer and adding 1
        # but if there is a wrap around at the end of the queue,
        # then the size is calculated by subtracting the front
        # pointer from the length of the queue and adding the
        # rear pointer to it and adding 1
        if front <= rear:
            print("Size:", rear - front + 1)
        else:
            print("Size:", len(queue) - front + rear + 1)

while True:
    print("1. Initialize")
    print("2. Enqueue")
    print("3. Dequeue")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        initialize()
    elif choice == 2:
        data = input("Enter the data: ")
        enqueue(data)
    elif choice == 3:
        data = dequeue()
        print("Dequeued element:", data)
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice!")