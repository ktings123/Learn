

from collections import deque

# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a + b


# word = ['cat', 'dog', 'resposebility', 'sun']
# for i in word[:]:
#     if len(i) > 5:
#         word.insert(2, i)
# print(word)


# 循环
# for n in range(10):
#     for i in range(1, n):
#         print(n, '*', i, '=', n * i)
#         break

# 列表
# que = deque(["sady","toyi","cat"])
# que.append("panda")
# print(que.pop())

# sque_dan=[-4,2,3,5]
# sque = [x*2 for x in sque_dan ]
# print(sque_dan)

# 删除
# ops = [123,32,5,786,123]
# del ops[2]
# print(ops)

# 拆分
# t=10
# z=20
# x,y = t,z
# print(x,y,t,z)
# q = [123,4324,67]
# o,j,k = q
# print(o,j)
# t,z,y = 10,20,30
# print(t,z,y)

# 字典
# phone = {'xiaomei': 7853497, 'jojo': 54353, 'gugu': 10567}
# del phone['xiaomei']
# print(phone)

# key和word
# form = {'john': 20, 'jane': 14, 'hode': 30}
# for j, k in form.items():
#     print(j, 'is ', k, 'years old')
# 索引和值
# for z, x in enumerate(form):
#     print(z, x)
# 同时遍历多个序列
# id = [1, 2, 3]
# name = ['po', 'kily', 'mast']
# age = [10, 30, 23]
# for n, m,l in zip(id, name, age):
#     print('{id}  {name} is {age} year old'.format(id=id, name=name, age=age))
# 反向遍历
# for k in reversed(range(1,10,2)):
#     print(k)
# 顺序排列
# lunch=['chicken','banana','tucker','pear']
# for g in sorted(lunch):
#     print(g)

# 文件操控
# o = open(r'C:/Users/82008947/Desktop/itop.txt','r',encoding='utf-8')
# print(o.read())
# o.close()

