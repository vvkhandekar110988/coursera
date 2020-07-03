def count(lst):
    c = 0
    for _ in lst:
        c += 1
    print(c)
    return str(c)


print('Number of elements are', count([1, 2, 7, 8, 10, 63, 41, 8, 9]))
