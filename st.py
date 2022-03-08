import csv
import math
file = open("class1.csv")
f = csv.reader(file)
data = list(f)
data.pop(0)
marks = []
for i in range(0,len(data)):
    value = int(data[i][1])
    marks.append(value)
sum = 0
for i in marks:
    sum = sum+int(i)
mean = sum/len(marks)
print(mean)
squares = []
for i in marks:
    a = int(i)-mean
    a = a**2
    squares.append(a)
sum = 0
for i in squares:
    sum = sum+int(i)
result = sum/(len(marks)-1)
sd = math.sqrt(result)
print(sd)

import statistics
print(statistics.stdev(marks))