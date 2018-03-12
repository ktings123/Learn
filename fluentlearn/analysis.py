# coding=utf-8


import numpy as np
import pandas as pd

# data1 = [1, 2, 3, 4, 5]
# array1 = np.array(data1)
# print(array1+1)
#
# data2 = [[1,2,3,4],[7,8,9]]
# array2 = np.array(data2)
# print(array2)

# series用法
# x = [1, 2, 3, 4, 5]
# s = pd.Series(x, index=['a', 'b', 'c', 'd', 'e'])
# print(s)
# print(s.index)

# Dataframe用法
table = {'name': ['dick', 'tim', 'jacky', 'nick', 'kate'],
         'age': [15, 20, 27, 25, 31],
         'sex': ['man', 'man', 'women', 'man', 'wonmen']}
# print(pd.DataFrame(table).info())

# 修改字段内容
seData = pd.DataFrame(table)
# seData['age'] = [2,3,4,5,6]
# print(seData)

# # 增加字段和内容
seData['country'] = ['china', 'canada', 'janpa', 'singapo', 'china']
# print(seData.index)
# print(seData[['name', 'age']])
# # 指定条件
# print(seData[seData.age > 3])
# print(seData[seData.country == 'china'])
# # 多条件筛选
# print(seData[(seData.age < 30) & (seData.age > 20)])
# seData.query("20<age<30")

# print(seData.iloc[1])
seData.index = [1, 2, 3, 4, 5]
# print(seData.loc[2])
print(seData.ix[[1,2], 'age'])