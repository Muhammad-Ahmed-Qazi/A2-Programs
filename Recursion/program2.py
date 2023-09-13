def something(num):
    if num == 7:
        some = 1
    else:
        some = something(num + 1) + num
    return some

print(something(4))