import calendar

y = int(input("Enter year : "))
m = int(input("Enter month : "))

if 12 >= m >= 1:
    print(calendar.month(y, m))
else:
    print("Enter Valid Month!")


