def largest(a, b, c):
    if a == b == c:
        return a
    else:
        if a > b:
            if a > c:
                return a
            else:
                return c
        else:
            if b > c:
                return b
            else:
                return c


x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
z = int(input("Enter Third Number :"))

print("Largest: ", largest(x, y, z))


