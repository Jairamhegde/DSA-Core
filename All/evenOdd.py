array = [3, 4, 6, 7, 1, 2]

i = 0
j = len(array) - 1

while i < j:
    if array[i] % 2 == 0:
        i += 1
    elif array[j] % 2 != 0:
        j -= 1
    else:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

print(array)
