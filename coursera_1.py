str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# str_1 = str_list[0]
# str_2 = list(str_1)
# print(str_2)
str_1 = []

for item in str_list:
    for i in range(len(item)):
        str_1 = list(item)
    print(len(str_1))