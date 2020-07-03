def last_four(x):
    print(x)
    for item in x:
        b = ''
        for i in item[-4:]:
            b = b + str(i)
        return int(b)




# print(last_four('123456789'))

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids = sorted(ids, key=last_four(ids))
