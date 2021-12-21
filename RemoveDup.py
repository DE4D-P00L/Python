a = [1, 16, 4, 9, 16, 25, 36, 49, 64, 81, 100, 16, 25, 36]


def remove_duplicate(lst):
    c = []
    for i in lst:
        if i not in c:
            c.append(i)
    return c


b = remove_duplicate(a)
print(b)
