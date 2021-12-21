n = int(input("Enter Number :"))
sumNum = 0
for i in range(n+1):
    for j in range(i):
        sumNum += n
print("Sum :", sumNum)
