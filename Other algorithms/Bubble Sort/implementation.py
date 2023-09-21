from colorama import Fore, Back, Style, init
init()

# arr = [4, 3, 2, 10, 12, 1, 5, 6]
arr = list()

master = 0
# slave = 0

count = 0
temp = 0
swap = True

def bubbleSort():
    global master, count, temp, swap, arr

    for count in range(0, len(arr)):
        for master in range(1, len(arr)):
            if arr[master - 1] > arr[master]:
                temp = arr[master]
                arr[master] = arr[master - 1]
                arr[master - 1] = temp
                swap = True
        if swap == False: break

while True:
    inp = int(input("Enter a number (-1 to stop): "))
    if inp == -1:
        break
    arr.append(inp)

bubbleSort()
print("Sorted array:")
print(Fore.GREEN + ">>>", arr, Style.RESET_ALL)