#! /usr/bin/en python
# coding=utf-8

import socket

l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
l.bind(('172.28.11.188', 443))
l.listen(5)
conn, add = l.accept()

print add, 'is connnecting........ !'
print conn.recv(1024)
conn.send('who are you!')

