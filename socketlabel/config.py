#! /usr/bin/env python
# coding=utf-8

import configparser, os

conFile = configparser.ConfigParser()
conFile.read(os.path.join(os.getcwd(), 'C:\Users\82008947\Desktop\Itop\config.conf'))
conff = {}
conff['sender'] = conFile.get('email', 'sender')
conff['receiver'] = conFile.get('email', 'receiver')
conff['smtpserver'] = conFile.get('email', 'smtpserver')
conff['username '] = conFile.get('email', 'username')
conff['password '] = conFile.get('email', 'password')

print conff