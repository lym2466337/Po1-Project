# file_name: test_abc.py

#setup 和 teardown主意分为 函数级别，类级别，模块级别
#函数级别：每个测试用例的函数运行一次开始或者结束都会执行一次

import pytest  # 引入pytest包
class Test_ST:


    def setup(self):
        print('>>setup')

    def teardown(self):
        print('>>teardown')

    def test_a(self):  # test开头的测试函数
        print("------->test_a")
        assert True  # 断言成功


    def test_b(self):
        print("------->test_b")
        assert False  # 断言失败


if __name__ == '__main__':
    pytest.main("-s  test_001_setup.py")  # 调用pytest的main函数执行测试