arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

lb = 0
ub = len(arr) - 1

def binSearch(val, lb, ub):
    mid = (lb + ub) // 2
    
    while lb <= ub:
        mid = (lb + ub) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            lb = mid + 1
        elif arr[mid] > val:
            ub = mid - 1
    
    return -1

inp = input("Enter a value to search for:\n>>> ")
result = binSearch(inp, lb, ub)

if result != -1:
    print("Value found at position: ", result + 1)
else:
    print("Value not found!")