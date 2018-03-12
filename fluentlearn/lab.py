# coding=utf-8

# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         return "Total Employee %d" % Employee.empCount
#
#     def displayEmployee(self):
#         print( "Name : ", self.name, ", Salary: ", self.salary)
#
# liyang = Employee('liyang','10k')
# liyang.displayEmployee()

# 循环简写
# num1 = [1, 2, 3, 4, 5, 6]
# num = [num for num in enumerate(num1,1)]
# print(num)

def is_odd(x):
    return x % 2 == 1


num = map(is_odd, [1, 4, 6, 7, 9, 12, 17])
print(type(num))
print(list(num))
