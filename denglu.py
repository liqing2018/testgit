from selenium import webdriver
import time
import re

driver = webdriver.Firefox()
url  = r"http://192.168.91.129/ecshop/"
driver.get(url)
driver.find_element_by_xpath(".//*[@id='ECS_MEMBERZONE']/a[1]/img").click()
driver.find_element_by_xpath("html/body/div[7]/div[1]/form/table/tbody/tr[1]/td[2]/input").send_keys("liqin")
driver.find_element_by_xpath("html/body/div[7]/div[1]/form/table/tbody/tr[2]/td[2]/input").send_keys("123456")
driver.find_element_by_xpath("html/body/div[7]/div[1]/form/table/tbody/tr[4]/td[2]  R/input[3]").click()
time.sleep(10)
title=driver.title
print (title)
print (driver.name)
page = driver.page_source
url_list = re.findall('href=\"(.*?)\"',page,re.S)
url_all = []
for url in url_list:
    if "http" in url:
        print (url)
        url_all.append(url)
print (url_all)


class Login_Blog():
    def __init__(self,driver):
        self.driver = driver
    def login(self,username,psw):
        self.driver.find_element_by_xpath("html/body/div[7]/div[1]/form/table/tbody/tr[1]/td[2]/input").send_keys("liqin")
        self.driver.find_element_by_xpath("html/body/div[7]/div[1]/form/table/tbody/tr[2]/td[2]/input").send_keys("123456")

import csv



