n = int(input("Enter Number: "))
isPrime = 1

for i in range(2, n):
    if n % i == 0:
        isPrime = 0

if isPrime:
    print(n, "is Prime!")
else:
    print(n, "is not Prime!")
