def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return True
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return False








print(checkingIfIn('pear'))
