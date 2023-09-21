from colorama import Fore, Back, Style, init
init()

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

found = False

inp = input("Enter a value to search for: ")

for count in range(0, len(arr)):
    if arr[count] == inp:
        found = True
        print(Fore.GREEN + "Value found at position:", count + 1, Style.RESET_ALL)
        break

if found == False:
    print(Fore.RED + "Value not found!", Style.RESET_ALL)