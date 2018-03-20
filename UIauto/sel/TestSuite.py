import unittest
from sel.TestCase import TestClass

if __name__ == '__main__':
    suite = unittest.TestSuite()
    begins = [TestClass("test_add"), TestClass("test_mul"), TestClass("test_min")]  # 测试用例装进列表里面
    suite.addTests(begins)  # 添加用例到测试套件
    with open('testReport.txt','a') as T:
        run = unittest.TextTestRunner(stream=T,verbosity=2)
        run.run(suite)  # 运行套件
