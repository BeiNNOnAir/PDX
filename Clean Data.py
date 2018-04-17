import csv
import re
import copy
with open("detail.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

for data in rows:
    a = copy.deepcopy(data)
    for i in data:
        keyword = re.findall('第.天|.*花费.*|前言|.*一篇.*|.*了.*|.*一条.*|.*旅行.*|.*购物.*|.*交通.*|.*住宿.*|.*美食.*|.*签证.*|.*引子.*|.*摄影.*|.*其他.*|.*遇到.*', i)
        if i in keyword:
            a.remove(i)
    with open('cleandata2.csv', 'a+', newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        writer.writerow(a)