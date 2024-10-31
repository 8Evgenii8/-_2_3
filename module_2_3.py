my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i= 0
n = my_list[i]

while i < len(my_list) and n >= 0:
    n = my_list[i]
    i = i + 1
    if n < 0:
        break
    elif i == 0:
        continue
    print(n)