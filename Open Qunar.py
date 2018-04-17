from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True

binary = FirefoxBinary(r'D:\tool\Fire\firefox.exe')

fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.image",2)
fp.set_preference("javascript.enabled", False)

driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps)
driver.get("http://you.ctrip.com/travels/shanghai2.html")

