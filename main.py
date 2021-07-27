import csv
import math
import pandas as pd

with open('data.csv',newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data = file_data[0]

def calculate_mean(file_data):
    total = 0
    length = len(file_data)

    for i in file_data:
        total += float(i)

    mean = total/length
    return mean

squared_list = []
for i in file_data:
    diff = float(i)-calculate_mean(file_data)
    square = diff**2
    squared_list.append(square)

sum = 0

for i in squared_list:
    sum += i

div = sum/(len(file_data)-1)
result = math.sqrt(div)

print("The standard deviation is " ,result)

