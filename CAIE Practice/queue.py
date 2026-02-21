SIZE = 10
NULL = -1

queue = [None for i in range(SIZE)]

head = tail = NULL
free = SIZE

def initialise():
    global head, tail, free

    for i in range(SIZE):
        queue[i] = None

    head = tail = NULL
    free = SIZE

def enqueue(data):
    global head, tail, free

    if free != NULL + 1:
        tail += 1
        queue[tail] = data
        if free == SIZE: head += 1
        print("Data stored!")
    else:
        print("Overflow error! Queue is full!")
