import csv

f = open("April.csv", "r")
reader = csv.reader(f)

# for row in reader:
#     print(row)

data = list(reader)
print(data)
print(data[6])
del data[:16]
del data[20:]
print(data)
print(data)