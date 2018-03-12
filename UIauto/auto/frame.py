#!/usr/bin/en python
# coding:utf -8


from selenium import webdriver
from selenium.webdriver.support.ui import Select

__author__ = "chris"


def frame(framename, framestatus, farameband, framemodel, uuid, framesn,
          framecountry, framecity, framedatacenter, frameidc, framerack, framestartpos):
    bro = webdriver.Firefox()
    bro.get("http://172.28.17.87/#/ajax/asset/frame/frameSearch")
    bro.find_element_by_css_selector("div.btn-group > button.btn.btn-primary").click()
    Select(bro.find_element_by_name("framename")).select_by_visible_text("{framename}".format(framename=framename))
    Select(bro.find_element_by_name("framestatus")).select_by_visible_text(
        "{framestatus}".format(framestatus=framestatus))
    Select(bro.find_element_by_name("farameband")).select_by_visible_text("{farameband}".format(farameband=farameband))
    Select(bro.find_element_by_name("framemodel")).select_by_visible_text("{framemodel}".format(framemodel=framemodel))
    bro.find_element_by_css_selector("button.btn").click()
    bro.find_element_by_css_selector("div.btn-group.pull-right > button.btn.btn-primary").click()
    bro.find_element_by_xpath("(//input[@type='text'])[10]").clear()
    bro.find_element_by_xpath("(//input[@type='text'])[10]").send_keys("{uuid}".format(uuid=uuid))
    bro.find_element_by_css_selector("#editUserModal > div.modal-dialog > div.mo"
                                     "dal-content > div.modal-footer > button.btn.btn-primary").click()
    bro.find_element_by_name("framesn").clear()
    bro.find_element_by_name("framesn").send_keys("{framesn}".format(framesn=framesn))
    Select(bro.find_element_by_name("framecountry")).select_by_visible_text(
        "{framecountry}".format(framecountry=framecountry))
    Select(bro.find_element_by_name("framecity")).select_by_visible_text("{framecity}".format(framecity=framecity))
    Select(bro.find_element_by_name("framedatacenter")).select_by_visible_text(
        "{framedatacenter}".format(framedatacenter=framedatacenter))
    Select(bro.find_element_by_name("frameidc")).select_by_visible_text("{frameidc}".format(frameidc=frameidc))
    Select(bro.find_element_by_name("framerack")).select_by_visible_text("{framerack}".format(framerack=framerack))
    Select(bro.find_element_by_name("framestartpos")).select_by_visible_text(
        "{framestartpos}".format(framestartpos=framestartpos))
    bro.find_element_by_xpath(u"//button[@value='下一步']").click()
    bro.find_element_by_xpath(u"//button[@value='确定']").click()
    bro.find_element_by_id("alertModal-confirm").click()
