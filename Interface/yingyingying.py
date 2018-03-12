#! /usr/bin/env python
# coding=utf-8

from __future__ import division
import sys, time, socket, glob, string, platform, itertools

# 多行输入
# text = ''
# while 1:
#     data = input(">>")
#     if data.strip()== 'stop':
#         break
#     text += "%s \n" % data
# print(text)

# 进度条
# j = '='
# for i in range(1,61):
#     j += '='
#     sys.stdout.write(str(int((i/60)*100))+'%  ||'+j+'->'+"\r")
#     sys.stdout.flush()
#     time.sleep(0.1)

# 通过域名获取ip
# ip = socket.getaddrinfo('www.baidu.com', 'http')[0][4]
# print(ip)

# 文件查找
# print(glob.glob(r'D:/apache-jmeter-3.2/*.txt'))

# 列表元素相加
# a = ['adc', 'defg', 'ijk']
# print(''.join(a))

# 嵌套列表转换成单表
# a = [[1, 2], [2, 3], [4, 5]]
# print(list(itertools.chain.from_iterable(a)))

# 断言
# try:
#     assert 1 == 0, 'is me!'
# except Exception as e:
#     print('%s' % e.__class__.__name__, e)







