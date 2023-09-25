from colorama import Fore, Back, Style, init
init()

import random as rnd
import string as st

N = 7

score = [rnd.randrange(0, 100) for i in range(249)]
name = list()

for i in range(0, 249):
    res1 = ''.join(rnd.choices(st.ascii_lowercase + st.ascii_uppercase, k=N))
    res2 = ''.join(rnd.choices(st.ascii_lowercase + st.ascii_uppercase, k=N))
    name.append([res1, res2])

# name = [list() for i in range(249)]

i = 0
j = 0

yearSize = 249

print("Unsorted array:")
print(Fore.RED + ">>>", score, Style.RESET_ALL)
print(Fore.RED + ">>>", name, Style.RESET_ALL)
print("\n")

for i in range(0, yearSize):
    key1 = score[i]
    key2 = name[i][0]
    key3 = name[i][1]

    j = i - 1

    while j >= 0 and key1 > score[j]:
        score[j + 1] = score[j]
        name[j + 1][0] = name[j][0]
        name[j + 1][1] = name[j][1]
        j -= 1
    
    score[j + 1] = key1
    name[j + 1][0] = key2
    name[j + 1][1] = key3

print("Sorted array:")
print(Fore.GREEN + ">>>", score, Style.RESET_ALL)
print(Fore.GREEN + ">>>", name, Style.RESET_ALL)