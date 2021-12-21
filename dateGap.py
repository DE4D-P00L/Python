import datetime

d1 = input("Enter Date 1: ")
d2 = input("Enter Date 2: ")

dd1, mm1, yy1 = map(int, list(d1.split("-")))
dd2, mm2, yy2 = map(int, list(d2.split("-")))

date1 = datetime.date(yy1,mm1,dd1)
date2 = datetime.date(yy2,mm2,dd2)

diff = date1-date2
print(abs(diff.days), "days")

