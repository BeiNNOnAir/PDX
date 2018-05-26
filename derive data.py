encoding = 'UTF-8'
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import csv
import time

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
binary = FirefoxBinary(r'D:\tool\Fire\firefox.exe')

fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.image", 2)
fp.set_preference("javascript.enabled", False)

driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps)


# 定义函数，因为数都存在这个class下【通过对比网页】
def outputresult(page_id, soup, output_list):
    for item in soup.find(class_='b_strategy_list '):
        try:
            title = item.find(class_='tit').a.text.strip()
        except:
            title = ''
        try:
            link = "http://travel.qunar.com"+item.find(class_='tit').a['href']
        except:
            link = ''
        try:
            date = item.find(class_='date').text.strip()
        except:
            date = ''
        try:
            days = item.find(class_='days').text.strip()
        except:
            days = ''

        if title != "":
            output_list.append([str(page_id), title, link,date,days])
    return output_list


for i in range(1, 1000):
    link = "http://travel.qunar.com/travelbook/list/22-shanghai-299878/hot_heat/"+str(i)+".htm"
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, "lxml")
    output_list = []
    output_list = outputresult(i, soup, output_list)

    with open('qunar.csv', 'a+', newline='', encoding='UTF-8') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerows(output_list)
    time.sleep(2)
