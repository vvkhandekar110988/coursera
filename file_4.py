fileref = open('../coursera/sample_files/travel_plans.txt', 'r')
contents = fileref.read()
print(type(contents))
num = 0
for i in contents:
    num += 1

print(num)

# str = contents.strip().split(' ')
# print(str)