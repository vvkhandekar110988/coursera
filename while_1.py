""" Write a function called stop_at_four that iterates through a list of numbers.
Using a while loop, append each number to a new list until the number 4 appears.
The function should return the new list. """


def stop_at_four(m):
    list1 = []
    i = 0
    while i < len(m):
        if m[i] != 4:
            list1.append(m[i])
        else:
            return list1
        i += 1
    return list1


print(stop_at_four([1, 6, 2, 3, 9]))
