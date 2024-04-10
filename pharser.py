import csv
from datetime import datetime

date = datetime.today().day
month: int = datetime.today().month
weekday = 4 # datetime.today().weekday() #날짜
weeknum = 0 # 주차
calandar = []

f = open("April.csv", "r", encoding="UTF-8")
reader = csv.reader(f)
sliceNum = [1, 10, 19, -1] # Location of data in list "Data"

data = list(reader)
print(len(data))
del data[:16] # Range of data
del data[29:]
print(data)

for i in data:
    if str(month)+"/" in i[0]:
        delIndex = data.index(i)
        del data[delIndex-7:delIndex]
        calandar.append(i)
        data.remove(i)

print(date) # date.test
print()
print(calandar)
print()
print(data)
print()

# 리스트 두개 합쳐서 키랑 데이터 형식으로 저장하기 ㅇㅇ

if weekday > 4:
    print("오늘은 주말입니다.") # is Weekend?
else:
    print(data[sliceNum[weeknum]][weekday-1])

