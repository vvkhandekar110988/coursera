fileref = open('../coursera/sample_files/emotion_words.txt', 'r')
contents = fileref.read()
print(contents)
str1 = contents.replace('\n', ' ')
num_words = 0
str = str1.strip().split(' ')


print(str)
for i in str:
    num_words += 1

print(num_words)
