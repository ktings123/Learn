#!/usr/bin/en python
# coding:utf -8


from selenium import webdriver
from selenium.webdriver.support.ui import Select

__author__ = "chris"


def network(netname, netstatus, netunit, netband, netmodel, netchangetype, ip, uuid,
            ntsn, ntservicetag, netcountry, netcity, netdatacenter, netidc, netrack, ntstartpos):
    bro = webdriver.Firefox()
    bro.get("http://172.28.17.87/#/ajax/asset/netDevice/netDeviceSearch")
    bro.find_element_by_css_selector("div.btn-group > button.btn.btn-primary").click()
    Select(bro.find_element_by_name("netname")).select_by_visible_text("{netname}".format(netname=netname))
    Select(bro.find_element_by_name("netstatus")).select_by_visible_text("{netstatus}".format(netstatus=netstatus))
    Select(bro.find_element_by_name("netunit")).select_by_visible_text("{netunit}".format(netunit=netunit))
    Select(bro.find_element_by_name("netband")).select_by_visible_text("{netband}".format(netband=netband))
    Select(bro.find_element_by_name("netmodel")).select_by_visible_text("{netmodel}".format(netmodel=netmodel))
    Select(bro.find_element_by_name("netchangetype")).select_by_visible_text(
        u"{netchangetype}".format(netchangetype=netchangetype))
    bro.find_element_by_name("ntip").clear()
    bro.find_element_by_name("ntip").send_keys("{ip}".format(ip=ip))
    bro.find_element_by_css_selector("button.btn").click()
    bro.find_element_by_css_selector("div.btn-group.pull-right > button.btn.btn-primary").click()
    bro.find_element_by_xpath("(//input[@type='text'])[16]").clear()
    bro.find_element_by_xpath("(//input[@type='text'])[16]").send_keys("{uuid}".format(uuid=uuid))
    bro.find_element_by_css_selector("#editUserModal > div.modal-dialog > div.modal-content > "
                                     "div.modal-footer > button.btn.btn-primary").click()
    bro.find_element_by_name("ntsn").clear()
    bro.find_element_by_name("ntsn").send_keys("{ntsn}".format(ntsn=ntsn))   # 序列号
    bro.find_element_by_name("ntservicetag").clear()
    bro.find_element_by_name("ntservicetag").send_keys("{ntservicetag}".format(ntservicetag=ntservicetag))  # 服务标签
    Select(bro.find_element_by_name("netcountry")).select_by_visible_text("{netcountry}".format(netcountry=netcountry))
    Select(bro.find_element_by_name("netcity")).select_by_visible_text("{netcity}".format(netcity=netcity))
    Select(bro.find_element_by_name("netdatacenter")).select_by_visible_text("{netdatacenter}".format(netdatacenter=netdatacenter))
    Select(bro.find_element_by_name("netidc")).select_by_visible_text("{netidc}".format(netidc=netidc))
    Select(bro.find_element_by_name("netrack")).select_by_visible_text("{netrack}".format(netrack=netrack))
    Select(bro.find_element_by_name("ntstartpos")).select_by_visible_text("{ntstartpos}".format(ntstartpos=ntstartpos))
    bro.find_element_by_name("ntnum_0").clear()
    bro.find_element_by_name("ntnum_0").send_keys("2")
    bro.find_element_by_name("ntspeed_0").clear()
    bro.find_element_by_name("ntspeed_0").send_keys("100")
    bro.find_element_by_xpath(u"//button[@value='下一步']").click()
    bro.find_element_by_xpath(u"//button[@value='确定']").click()
    bro.find_element_by_xpath(u"(//button[@value='确定'])[2]").click()
    bro.find_element_by_id("alertModal-confirm").click()


