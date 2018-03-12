#!/usr/bin/en python
# coding:utf -8


from selenium import webdriver
from selenium.webdriver.support.ui import Select

__author__ = "chris"


def network(name, status, uuid, height, brand, model, serial, servicetag,
            country, city, datacenter, idc, rack, startpos, ip):
    bro = webdriver.Firefox()
    bro.get("http://172.28.17.87/#/ajax/asset/server/serverSearch")
    bro.find_element_by_css_selector("div.btn-group > button.btn.btn-primary").click()
    Select(bro.find_element_by_name("name")).select_by_visible_text("{name}".format(name=name))
    Select(bro.find_element_by_name("status")).select_by_visible_text("{status}".format(status=status))
    bro.find_element_by_css_selector("button.btn").click()
    bro.find_element_by_css_selector("div.btn-group.pull-right > button.btn.btn-primary").click()
    bro.find_element_by_xpath("(//input[@type='text'])[19]").clear()
    bro.find_element_by_xpath("(//input[@type='text'])[19]").send_keys("{uuid}".format(uuid=uuid))
    bro.find_element_by_css_selector("div.modal-footer > button.btn.btn-primary").click()
    Select(bro.find_element_by_name("height")).select_by_visible_text("{height}".format(height=height))
    Select(bro.find_element_by_name("brand")).select_by_visible_text("{brand}".format(brand=brand))
    Select(bro.find_element_by_name("model")).select_by_visible_text("{model}".format(model=model))
    bro.find_element_by_name("serial").clear()
    bro.find_element_by_name("serial").send_keys("{serial}".format(serial=serial))
    bro.find_element_by_name("servicetag").clear()
    bro.find_element_by_name("servicetag").send_keys("{servicetag}".format(servicetag=servicetag))
    Select(bro.find_element_by_name("country")).select_by_visible_text("{country}".format(country=country))
    Select(bro.find_element_by_name("city")).select_by_visible_text("{city}".format(city=city))
    Select(bro.find_element_by_name("datacenter")).select_by_visible_text("{datacenter}".format(datacenter=datacenter))
    Select(bro.find_element_by_name("idc")).select_by_visible_text("{idc}".format(idc=idc))
    Select(bro.find_element_by_name("rack")).select_by_visible_text("{rack}".format(rack=rack))
    Select(bro.find_element_by_name("startpos")).select_by_visible_text("{startpos}".format(startpos=startpos))
    bro.find_element_by_xpath("(//button[@type='button'])[3]").click()
    bro.find_element_by_xpath("(//button[@type='button'])[5]").click()
    bro.find_element_by_name("name_0").clear()
    bro.find_element_by_name("name_0").send_keys("{ip}".format(ip=ip))
    bro.find_element_by_xpath("(//button[@type='button'])[9]").click()
    bro.find_element_by_id("alertModal-confirm").click()
