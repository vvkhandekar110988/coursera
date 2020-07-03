def mylen(seq):
    c = 0
    for _ in seq[3:7]:
        c += 1

    return c


print(mylen('vi'))
lst = [1, 2, 7, 8, 10, 63, 41, 8, 9]
print(len(lst))
print(mylen(lst))
