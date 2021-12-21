import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
y = datetime.datetime.today().year
print(name, "you will turn 100 years old in year", y+100-age)
