def test(int1, bool1 = True, dict1 = {2:3, 4:5, 6:8}):
    bool1 = True
    if bool1:
        for p in dict1.items():
            if int1 == p[0]:
                return p[1]
    else:
        return False

print(test(4, False))

print(test(5, dict1 = {5:4, 2:1}))