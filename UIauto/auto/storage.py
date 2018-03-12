#!/usr/bin/en python
# coding:utf -8


from selenium import webdriver
from selenium.webdriver.support.ui import Select

__author__ = "chris"


def storage(netname, storestatus, uuid, ):
    bro = webdriver.Firefox()
    bro.get("")
    bro.find_element_by_css_selector("div.btn-group > button.btn.btn-primary").click()
    Select(bro.find_element_by_name("netname")).select_by_visible_text("{netname}".format(netname=netname))
    Select(bro.find_element_by_name("storestatus")).select_by_visible_text("{storestatus}".format(storestatus=storestatus))
    bro.find_element_by_css_selector("button.btn").click()
    bro.find_element_by_css_selector("div.btn-group.pull-right > button.btn.btn-primary").click()
    bro.find_element_by_xpath("(//input[@type='text'])[17]").clear()
    bro.find_element_by_xpath("(//input[@type='text'])[17]").send_keys("{uuid}".format(uuid=uuid))