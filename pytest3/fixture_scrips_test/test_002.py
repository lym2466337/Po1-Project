import pytest

@pytest.fixture()
def init_fuc():
    with open("./data.txt","w") as f:
        f.write("2")
    print("..运行fixture标记方法")

#fixture作用域为函数方法使用方式第二种--放在类的前面添加标记 @pytest.mark.usefixtures(fixture方法名的 字符串)，则在这个测试类中的每一个测试方法用例运行前都会先运行fixture的方法
#也可以自己放在类中的测试用例前，这种方式则只有在这个用例运行前才会运行，其他用例不会运行
@pytest.mark.usefixtures("init_fuc")
class Test_b:
    def test001(self):
        with open("./data.txt","r") as f:
            assert f.read()=="1"

    def test002(self):
        assert True