import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#Pytest控制函数执行顺序
# 默认情况下，pytest是根据测试方法名由小到大执行的,可以通过第三方插件包改变其运行顺序。
# 标记于被测试函数上方，@pytest.mark.run(order=x)
#         2.根据order传入的参数来解决运行顺序
#         3.order值全为正数或全为负数时，运行顺序：值越小，优先级越高
#         4.正数和负数同时存在：正数优先级高
class Test_1():
    def setup_class(self):

        desired_caps={
            'platformName': 'Android',  # 被测手机是安卓
            'platformVersion': '7.1.2',  # 手机安卓版本
            'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
            'appPackage': 'com.android.settings',  # 启动APP Package名称
            'appActivity': '.Settings',  # 启动Activity名称
            'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
           # 'noReset': True,  # 不要重置App，特别注意 对于启动缓慢的APP，需要先打开过APP后，再使用软件打开APP才能正常打开
            'newCommandTimeout': 6000,  # 设置等待APP无响应时间,必须设置
            'automationName': 'UiAutomator2'
            # 'app': r'd:\apk\bili.apk',
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        print("-->setup_class")
    def teardown_class(self):
        self.driver.quit()
        print("-->teardown_class")

    def wait_ele(self,tag,var):
        if tag=="xpath":
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(var))
        if tag=="id":
        if tag=="class":
            return WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element_by_class_name(var))
    #使用插件进行特殊排序  pytest.mark.run(order=x)
    @pytest.mark.run(order=2)
    def test_001(self):
        self.wait_ele("xpath","//*[contains(@text,'更多')]").click()
        self.wait_ele("xpath","//*[contains(@text,'移动')]").click()
        self.wait_ele("xpath","//*[contains(@text,'首选')]").click()
        self.wait_ele("xpath","//*[contains(@text,'2G')]").click()

        sum_list = self.driver.find_elements_by_id("android:id/summary")
        name_list=[i.text for i in sum_list]
        assert "3G" in name_list

    @pytest.mark.run(order=1)
    def test_002(self):
        assert True

    @pytest.mark.run(order=-1)
    def test_003(self):
        assert False

