import pytest
from appium import webdriver

#测试程序时尽量使用pytest的命令行形式，需要先cd到文件的路径，在使用pytest指令运行，调试的时候使用run 方式
# setup,teardown 类级别：只在类被运行的时候运行一次，不受函数运行次数影响
from selenium.webdriver.support.wait import WebDriverWait
# pytest --html=./rep.html   在指定目录下输出pytest的测试报告


class Test_ST1:
    def setup_class(self):
        print('这是setup——class')
        desired_caps = {
            'platformName': 'Android',  # 被测手机是安卓
            'platformVersion': '7.1.2',  # 手机安卓版本
            'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
            'appPackage': 'com.android.settings',  # 启动APP Package名称
            'appActivity': '.Settings',  # 启动Activity名称
            'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
            'noReset': True,  # 不要重置App，特别注意 对于启动缓慢的APP，需要先打开过APP后，再使用软件打开APP才能正常打开
            'newCommandTimeout': 6000,  # 设置等待APP无响应时间,必须设置
            'automationName': 'UiAutomator2'
            # 'app': r'd:\apk\bili.apk',
        }

        # 连接Appium Server，初始化自动化环境
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    #在类运行结束后，关闭driver
    def teardown_class(self):
        print(">>teardown")
        self.driver.quit()

    def wait_ele_by_xpth(self,xpath):
        return WebDriverWait(self.driver,5,0.5).until\
            (lambda x:x.find_element_by_xpath(xpath))
    def test_vpn(self):


    def test_2G(self):
        # WebDriverWait(self.driver,5,0.5).until\
        #     (lambda x:x.find_element_by_xpath("//*[contains(@text,'更多')]")).click()
        # WebDriverWait(self.driver,5,0.5).until\
        #     (lambda x:x.find_element_by_xpath("//*[contains(@text,'移动')]")).click()
        # WebDriverWait(self.driver,5,0.5).until\
        #     (lambda x:x.find_element_by_xpath("//*[contains(@text,'首选')]")).click()
        #
        # WebDriverWait(self.driver, 5, 0.5).until \
        #     (lambda x: x.find_element_by_xpath("//*[contains(@text,'3G')]")).click()
        self.wait_ele_by_xpth("//*[contains(@text,'更多')]").click()
        self.wait_ele_by_xpth("//*[contains(@text,'移动')]").click()
        self.wait_ele_by_xpth("//*[contains(@text,'首选')]").click()
        self.wait_ele_by_xpth("//*[contains(@text,'3G')]").click()

        #获取所有描述信息，并断言判断3g是否在描述信息内
        sum_list = self.driver.find_elements_by_id("android:id/summary")
        #使用列表推导式，将sum_list中所有的信息取text并存入一个新的列表
        test_list= [i.text for i in sum_list]

        #assert 需要被判断的函数, 判断失败的信息提示（有默认提示）
        assert '2G' in test_list,"失败了。。。。"

    # def test_002(self):
    #
    #     assert True


if __name__ == '__main__':
    pytest.main('-s test003_1.py')