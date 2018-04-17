from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
binary = FirefoxBinary(r'D:\tool\Fire\firefox.exe')
# 把上述地址改成你电脑中Firefox程序的地址
driver = webdriver.Firefox(firefox_binary=binary, capabilities=caps)
driver.get("http://you.ctrip.com/travels/shanghai2.html")