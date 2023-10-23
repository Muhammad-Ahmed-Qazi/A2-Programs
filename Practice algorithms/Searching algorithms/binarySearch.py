# Constants
SIZE = int(input("Enter length of array you want to create:\n>>> "))
print()

# Array declaration
arr = [None for i in range(SIZE)]
for i in range(SIZE):
    arr[i] = int(input("Enter any integer value: "))
print()

# Sorting array for binary search to work
arr.sort()
print(arr)

# Binary search function
def binSearch(val):    
    # Local variables
    upperBound = 0
    lowerBound = SIZE - 1
    
    while upperBound < lowerBound:
        mid = int((upperBound + lowerBound) / 2)
        print(arr[mid])
        if arr[mid] == val:
            return mid
        else:
            if val < mid:
                lowerBound = mid - 1
            elif val > mid:
                upperBound = mid + 1
        print()
    return False

# Main program
while True:
    found = False
    print("Enter a value to search for in the array:\n(Enter 'N' to exit the program)")
    userInp = input(">>> ")
    if userInp == 'N':
        print("Exiting program...")
        break
    result = binSearch(int(userInp))
    if result != False:
        print("Value found at index =", result)
    else:
        print("Value not found!")
