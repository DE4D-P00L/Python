a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

def smallest(x,y):
    if x < y:
        return x
    elif x > y:
        return y
    else:
        return x

for i in range(1,smallest(a,b)+1):
    if a % i == 0 and b % i == 0:
        hcf = i
    
print("HCF(",a,",",b,") = ",hcf)