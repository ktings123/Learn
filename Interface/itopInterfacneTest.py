#! /usr/bin/env python
# coding=utf-8

import requests
import Excel

excelMethod = Excel.method
excelData = Excel.data
excelUrl = Excel.url


# header = {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate',
#           'Accept - Language': 'zh - CN, zh;q = 0.8', 'Connection': 'keep-alive', 'Content-Length': '88',
#           'Content - Type': 'application / x - www - form - urlencoded;charset = UTF - 8', 'Host': '//172.28.17.87',
#           'Origin:http': '//172.28.17.87',
#           'Referer': 'http: // 172.28.17.87/',
#           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                         'Chrome/57.0.2987.133 Safari/537.36'}


class interFace:
    def __init__(self, method, url, parms):
        self.method = method
        self.url = url
        self.parms = eval(parms)

    def request(self):
        if self.method == 'post':
            ops = requests.session()
            re = ops.post(self.url, self.parms)
            return re
        if self.method == 'get':
            ops = requests.session()
            re = ops.get(self.url)
            return re

    def getJsession(self):
        seId = interFace.request(self).json().get('c').get('JSESSIONID')
        return seId

    def getlinStatus(self):
        code = interFace.request(self).json().get('s')
        return code

    def keepLink(self):
        if interFace.getlinStatus(self) == -100:
            login = interFace("get", "http://172.28.17.87:8080/itop-war/user/login", "{'username': 'admin', 'password': '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'}")
            seId = login.getJsession()

        else:
            return True

test = interFace(excelMethod, excelUrl, excelData)
print(test.request().json())
#print(type(test.getlinStatus()))
# print(test.request().status_code)
# print(test.getJsession())
#print(test.keepLink())
