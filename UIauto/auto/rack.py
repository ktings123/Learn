#!/usr/bin/en python
# coding:utf -8

__author__ = "chris"

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def rack(rackname, rackstatus, racksafebox, rackband, rackmodel, rackfullbox,usrID,
         rackcountry, rackcity, rackdatacenter, rackidc, rackrow,rackcol):
    bro = webdriver.Firefox()
    bro.get("http://172.28.17.87/#/ajax/asset/rack/rackSearch")
    bro.find_element_by_css_selector("div.btn-group > button.btn.btn-primary").click()
    bro.find_element_by_name("rackname").click()
    bro.find_element_by_name("rackname").send_keys("{rackname}".format(rackname=rackname))
    Select(bro.find_element_by_name("rackstatus")).select_by_visible_text("{rackstatus}".format(rackstatus=rackstatus))
    Select(bro.find_element_by_name("racksafebox")).select_by_visible_text("{racksafebox}".format(racksafebox=racksafebox))
    Select(bro.find_element_by_name("rackband")).select_by_visible_text("{rackband}".format(rackband=rackband))
    Select(bro.find_element_by_name("rackmodel")).select_by_visible_text("{rackmodel}".format(rackmodel=rackmodel))
    Select(bro.find_element_by_name("rackfullbox")).select_by_visible_text("{rackfullbox}".format(rackfullbox=rackfullbox))
    bro.find_element_by_css_selector("button.btn").click()
    bro.find_element_by_css_selector("div.btn-group.pull-right > button.btn.btn-primary").click()
    bro.find_element_by_xpath("(//input[@type='text'])[15]").clear()
    bro.find_element_by_xpath("(//input[@type='text'])[15]").send_keys("{usrID}".format(usrID=usrID))
    bro.find_element_by_css_selector("#editUserModal > div.modal"
                                     "-dialog > div.modal-content > div.modal-footer > button.btn.btn-primary").click()
    Select(bro.find_element_by_name("rackcountry")).select_by_visible_text("{rackcountry}".format(rackcountry=rackcountry))
    Select(bro.find_element_by_name("rackcity")).select_by_visible_text("{rackcity}".format(rackcity=rackcity))
    Select(bro.find_element_by_name("rackdatacenter")).select_by_visible_text("{rackdatacenter}".format(rackdatacenter=rackdatacenter))
    Select(bro.find_element_by_name("rackidc")).select_by_visible_text("{rackidc}".format(rackidc=rackidc))
    bro.find_element_by_name("rackrow").clear()
    bro.find_element_by_name("rackrow").send_keys("{rackrow}".format(rackrow=rackrow))
    bro.find_element_by_name("rackcol").clear()
    bro.find_element_by_name("rackcol").send_keys("{rackcol}".format(rackcol=rackcol))
    bro.find_element_by_xpath(u"//button[@value='下一步']").click()
    bro.find_element_by_xpath(u"//button[@value='确定']").click()
    bro.find_element_by_id("alertModal-confirm").click()









