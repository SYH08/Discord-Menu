import csv
from datetime import datetime

date = datetime.today().day
weekday = 4 #datetime.today().weekday()
weeknum = 0

f = open("April.csv", "r")
reader = csv.reader(f)
sliceNum = [1, 10, 19, -1]

data = list(reader)
print(len(data))
del data[:16]
del data[29:]
print(data)

data = list(filter(None, data))
print()
print(data[10][0])

l = 1
menu = []
print()
print(data[sliceNum[1]][4])
print()

print(menu)

print(date)

if weekday > 4:
    print("오늘은 주말입니다.")
else:
    print(data[sliceNum[weeknum]][weekday-1])