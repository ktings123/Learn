#!/usr/bin/en python
# coding:utf -8


from selenium import webdriver
from selenium.webdriver.support.ui import Select

__author__ = "chris"


# 新建数据中心和对应机房
def create(idc, lv, idcorg, country, city, address, selfgrade,
           idc_name, org, status, floor, line, bandwidth, idcteam,
           teamlv):
    bro = webdriver.Firefox()
    bro.get("http://172.28.17.87/#/ajax/asset/dataCenter/roomSearch")
    bro.find_element_by_css_selector("span.text").click()
    bro.find_element_by_name("dcname").clear()
    bro.find_element_by_name("dcname").send_keys("{idc}".format(idc=idc))
    Select(bro.find_element_by_name("dclevel")).select_by_visible_text("{lv}".format(lv=lv))
    Select(bro.find_element_by_name("dcorg")).select_by_visible_text("{idcorg}".format(idcorg=idcorg))
    Select(bro.find_element_by_name("dccountry")).select_by_visible_text("{country}".format(country=country))
    Select(bro.find_element_by_name("dccity")).select_by_visible_text("{city}".format(city=city))
    bro.find_element_by_name("dcaddress").clear()
    bro.find_element_by_name("dcaddress").send_keys("{address}".format(address=address))
    Select(bro.find_element_by_name("dcselfgrade")).select_by_visible_text("{selfgrade}".format(selfgrade=selfgrade))
    bro.find_element_by_css_selector("div.modal-footer > button.btn.btn-primary").click()
    bro.find_element_by_id("alertModal-confirm").click()
    bro.find_element_by_xpath("//tr[4]/td").click()  # 某选择数据中心，后续需要修改
    bro.find_element_by_name("idcname").clear()
    bro.find_element_by_name("idcname").send_keys("{idc_name}".format(idc_name=idc_name))
    Select(bro.find_element_by_name("idcorg")).select_by_visible_text("{org}".format(org=org))
    Select(bro.find_element_by_name("idcstatus")).select_by_visible_text("{status}".format(status=status))
    bro.find_element_by_name("idcfloor").clear()
    bro.find_element_by_name("idcfloor").send_keys("{floor}".format(floor=floor))
    bro.find_element_by_name("name_details0").clear()
    bro.find_element_by_name("name_details0").send_keys("{line}".format(line=line))
    bro.find_element_by_name("band_details0").clear()
    bro.find_element_by_name("band_details0").send_keys("{bandwidth}".format(bandwidth=bandwidth))
    Select(bro.find_element_by_name("idcteam")).select_by_visible_text("{idcteam}".format(idcteam=idcteam))
    Select(bro.find_element_by_name("idcteamlevel")).select_by_visible_text("{teamlv}".format(teamlv=teamlv))
    bro.find_element_by_xpath("//button[@value='确定']").click()
    bro.find_element_by_xpath("(//button[@value='确定'])[2]").click()
    bro.find_element_by_id("alertModal-confirm").click()




