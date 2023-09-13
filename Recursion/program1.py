def calc(x):
    temp = 1
    if x > 0:
        temp = x + calc(x - 2)
    else:
        temp = 0
    return temp

x = int(input("Enter a number: "))

print(calc(x))
