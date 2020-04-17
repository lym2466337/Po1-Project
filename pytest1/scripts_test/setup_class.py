import pytest
from appium import webdriver

#setup,teardown 类级别：只在类被运行的时候运行一次，不受函数运行次数影响
class Test_ST1:
    def setup_class(self):
        pass
    def teardown_class(self):

        print(">>teardown")

    def test_001(self):
        assert True
    def test_002(self):
        assert True

if __name__ == '__main__':
    pytest.main('-s test_02_setup_class.py')