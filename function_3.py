def addit(num1):
    global abc
    abc = num1 + 5


def mult(num2):
    result = num2 * abc
    return result


a = int(input('Enter number for addition '))
b = int(input('Enter number for multiplication '))

addit(a)

result1 = mult(b)

print('Result is {}'.format(result1))
