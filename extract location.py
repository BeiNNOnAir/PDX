import csv
with open("data_1.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
lists=[]
for i in rows:
    if reader.line_num == 1:  # 由于第一行为变量名称，故忽略掉
        continue
    for location in i:
        if location in lists:
            pass
        else:
            lists.append(location)

print(lists,len(lists))

'新天地', '田子坊', '上海迪士尼', '上海海洋水族馆', '上海影视乐园', '外滩', '上海城隍庙', '上海野生动物园', '上海科技馆', '豫园', '上海博物馆', '1933老场坊', '陆家嘴', '南京路步行街', '上海自然博物馆', '中华艺术宫', '上海汽车博物馆', '上海电影博物馆', '上海欢乐谷', '上海植物园', '上海动物园', '上海城市规划展示馆', '辰山植物园', '上海鲜花港', '再见，上海', '徐家汇藏书楼', '宋庆龄故居', '巴金寓所', '上海图书馆', '回家啦', '上海朱家角古镇', '东平国家森林公园', '杭州-上海(G7320)', '虹桥火车站-浦东机场(2号线)', '上海-大连(9C8977)'