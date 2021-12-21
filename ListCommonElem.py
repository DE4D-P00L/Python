a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
z = []

for e1 in a:
    for e2 in b:
        if e1 == e2:
            c.append(e1)

# Remove Duplicates
for e in c:
    if e not in z:
        z.append(e)

print(z)

