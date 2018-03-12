#!/usr/bin/env python
# coding=utf-8
# coding=utf8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #与服务器建立连接
s.connect(('172.28.11.188', 222))
    # 2. 构建请求行，请求资源是 index.php
request_line = b"GET /index.php HTTP/1.1"
    # 3. 构建请求首部，指定主机名
headers = b"Host: 172.28.17.87"
    # 4. 用空行标记请求首部的结束位置
blank_line = b"\r\n"
# 请求行、首部、空行这3部分内容用换行符分隔，组成一个请求报文字符串
# 发送给服务器
message = b"\r\n".join([request_line, headers, blank_line])
s.send(message)

# 服务器返回的响应内容稍后进行分析
response = s.recv(1024)
print(response)

