import csv
from datetime import datetime

date = datetime.today().day
weekday = 4 #datetime.today().weekday() #날짜
weeknum = 0 #주차

f = open("April.csv", "r")
reader = csv.reader(f)
sliceNum = [1, 10, 19, -1] #Location of data in list "Data"

data = list(reader)
print(len(data))
del data[:16] #Range of data
del data[29:]
print(data)

print()
print(data[10][0]) #test.1

print()
print(data[sliceNum[1]][4]) #test.2
print()

print(date) #date.test

if weekday > 4:
    print("오늘은 주말입니다.") #is Weekend?
else:
    print(data[sliceNum[weeknum]][weekday-1])

