def addition_index(mylist, i, length):
    if i == length - 1:
        return mylist[i]
    if i == 0:
        return (mylist[i] + addition_index(mylist, i + 1, length)) / 3
    else:
        return mylist[i] + addition_index(mylist, i + 1, length)


result = addition_index([1, 2, 3], 0, 3)
print(result)
