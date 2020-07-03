fileref = open("../coursera/sample_files/olympics.txt", "r")
lines = fileref.readlines()

for item in lines[:4]:
    print(item.strip())

fileref.close()
