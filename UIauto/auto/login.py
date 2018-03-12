#!/usr/bin/en python
# coding:utf -8


from selenium import webdriver
import time

__author__ = "chris"

# 输入账号密码登录
def inTo(username, password):
    bro = webdriver.Firefox()
    # bro.implicitly_wait(30)
    bro.get("http://172.28.17.87/#/")
    time.sleep(2)
    bro.find_element_by_name("username").send_keys("{name}".format(name=username))
    # bro.find_element_by_name("username").send_keys("admin")
    bro.find_element_by_name("password").send_keys("{pwd}".format(pwd=password))
    # bro.find_element_by_name("password").send_keys("123456")
    bro.find_element_by_id("btnLoin").click()




