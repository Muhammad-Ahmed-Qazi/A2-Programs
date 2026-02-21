"""
- Binary search
- Linear search
- Insertion sort
- Bubble sort
"""

array = [42, 7, 89, 23, 56, 14, 67, 34, 72, 11, 98, 3, 77, 50, 29]
# array.sort()

# Binary Search
def binarySearch(value):
    head = 0
    tail = len(array) - 1

    while head <= tail:
        mid = (head + tail) // 2

        if value == array[mid]:
            return mid
        elif value < array[mid]:
            tail = mid - 1
        elif value > array[mid]:
            head = mid + 1

    return None

def recursiveBinSearch(head, value, tail):
    if head <= tail:
        mid = (head + tail) // 2

        if value == array[mid]: return mid
        elif value < array[mid]:
            return recursiveBinSearch(head, value, mid - 1)
        else:
            return recursiveBinSearch(mid + 1, value, tail)
    else:
        return None

# Linear search
def linearSearch(value):
    for item in range(len(array)):
        if value == array[item]:
            return item
    
    return None

# Bubble sort
def bubbleSort():
    n = len(array)

    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
        if not swap: break

# Insertion sort
def insertionSort():
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            print(array)
        array[j + 1] = key



# while True:
print(array)
# inp = int(input("Enter value to search for: "))
insertionSort()
print(array)