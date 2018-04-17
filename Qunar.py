import requests
from bs4 import BeautifulSoup
link = "http://travel.qunar.com/travelbook/list/22-shanghai-299878/hot_heat/1.htm"
headers = {'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.1;en-US:rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
# Previously the code behind find function is .a.text.strip the result is None.
# Because .a function return none value so that the following code doesn't work.
# After change the code to the .string it works
title = soup.find("a", class_="tit").string

print(title)
