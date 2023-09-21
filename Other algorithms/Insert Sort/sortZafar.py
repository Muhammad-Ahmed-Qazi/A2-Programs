from colorama import Fore, Back, Style, init
init()

# arr = [4, 3, 2, 10, 12, 1, 5, 6]
arr = list()

master = 1
slave = 0
step = 0

def insertionSort():
    global arr, master, slave, step
    temp = 0

    for master in range(1, len(arr)):
        for slave in range(0, master):
            if arr[master] < arr[slave]:
                temp = arr[master]
                for step in range(master, slave, -1):
                    arr[step] = arr[step - 1]
                arr[slave] = temp
                break

while True:
    inp = int(input("Enter a number (-1 to stop): "))
    if inp == -444:
        break
    arr.append(inp)

insertionSort()
print("Sorted array:")
print(Fore.GREEN + ">>>", arr, Style.RESET_ALL)