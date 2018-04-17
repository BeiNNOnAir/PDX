encoding = 'UTF-8'
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import csv
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
binary = FirefoxBinary(r'D:\tool\Fire\firefox.exe')

fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.image", 2)
fp.set_preference("javascript.enabled", False)

driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps)


with open('qunar.csv', encoding='UTF-8') as f:
    csv_file = csv.reader(f)
    link_list = [[row[1],row[2]] for row in csv_file]

for eachone in link_list:
    name = eachone[0]
    link = eachone[1]
    output_list = []
    driver.get(link)
    locator = (By.CLASS_NAME, 'js_jump')
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
    soup = BeautifulSoup(driver.page_source, "lxml")
    output_list=[name,link]
    place_list=[]
    for eachones in soup.find_all("a", {"class":"js_jump"}):
        try:
            places = eachones.get('title')

            output_list.append(places)
        except:
            pass


    with open('detail.csv', 'a+', newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        writer.writerow(output_list)
    time.sleep(0.1)
