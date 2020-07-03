fileref = open('../coursera/sample_files/school_prompt.txt', 'r')
lines = fileref.readlines()
# contents = fileref.read()
# print(contents)
three = []
# print(lines)
for item in lines[:]:
    str1 = item.replace('\n',' ')
    str_list = str1.split(' ')
    # print(str_list)
    for item in str_list[2:3]:
        three.append(item)
print(three)

