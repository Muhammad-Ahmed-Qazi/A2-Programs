from colorama import Fore, Back, Style, init
init()

arr = [4, 3, 2, 10, 12, 1, 5, 6]

def insertionSort():
    global arr
    i = 0
    j = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(i, key, j)
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
        arr[j + 1] = key

insertionSort()
print("Sorted array:")
print(Fore.GREEN + ">>>", arr, Style.RESET_ALL)