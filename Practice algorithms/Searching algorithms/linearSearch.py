# Constants
SIZE = int(input("Enter length of array you want to create:\n>>> "))
print()

# Array declaration
arr = [None for i in range(SIZE)]
for i in range(SIZE):
    arr[i] = int(input("Enter any integer value: "))
print()

# Main program
while True:
    found = False
    print("Enter a value to search for in the array:\n(Enter 'N' to exit the program)")
    userInp = input(">>> ")
    if userInp == 'N':
        print("Exiting program...")
        break
    try:
        userInp = int(userInp)
    except:
        print("Value not an integer! Please try again!")
    for i in range(0, SIZE):
        if arr[i] == userInp:
            found = True
            print("Value found at index =", i)
    if found == False: print("Value not found!")
    print()
