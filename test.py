import csv
import re
import copy
with open("detail3.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

for data in rows:
    a = copy.deepcopy(data)
    for i in data:
        keyword = re.findall('第.天|.*花费.*|前言|.*一篇.*|.*了.*|.*一条.*|.*旅行.*', i)
        if i in keyword:
            a.remove(i)
    print(a)
