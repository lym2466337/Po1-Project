import pytest

#将该方法标记为fixture（该方法即称为  工厂函数），可以在运行测试方法，类，模块前，特别先运行下面的方法。该方式经常用于数据库建立链接
#不同于setup setupclass ，fixture更加灵活

"""
    方法：fixture(scope="function", params=None, autouse=False, ids=None, name=None)
    常用参数:
        scope：被标记方法的作用域
            function" (default)：作用于每个测试方法，每个test都运行一次
            "class"：作用于整个类，每个class的所有test只运行一次
            "module"：作用于整个模块，每个module的所有test只运行一次
            "session：作用于整个session(慎用)，每个session只运行一次
        params：(list类型)提供参数数据，供调用标记方法的【函数】使用
                搭配返回值为 request.param使用时，用例在用到返回值时，如果返回值是多个数据，断言的时候会将每个返回数据都断言一次
                而不是平时断言失败就结束使用返回值，不使用后面的数据
            测试用例在使用被标记方法的参数方式：
            普通方式：
            @pytest.fixture()
            def 被标记方法（）：
                return [1,2,3]
            
            传入params方式,request这里是固定用法：
            @pytest.fixture(params[1,2,3])
            def 被标记方法（request）：
                return request.param
            
            后面再测试用例使用被标记方法中，必须使用传入被标记方法名称参数的方式：   
            def 用例（被标记方法名称 字符串）
                assert 被标记方法 == 4
                这里的断言如果是普通方式，则在读到被标记方法的返回参数 1时就会停止
                如果是传入 params方式，则会使用被标记方法的1，2，3三个 数据都分别进行断言，即执行3次测试用例
                
                
        autouse：是否自动运行,默认为False不运行，设置为True自动运行，自动运行的时候  类、方法。。前不需要再加标记，会自动运行被标记的方法
        
    在使用fixture的作用域为 模块、session时，需要将被标记的方法写入 conftest.py（文件名固定，pytest只识别这个作为模块和session用）
    这样在调用时，pytest会优先调用这边的文件运行
"""

@pytest.fixture()
def init_fun():
    with open("./data.txt","w") as f:
        f.write("3")
    print("...初始化清理数据库 init_fixture")

#作用域为函数方法第一种使用方式：在测试用例中，当做参数传入被标记为 fixture的方法名
class Test_A:
    #测试用例传入参数 init_fun  即fixture标记的方法名
    def test001(self,init_fun):
        with open("./data.txt","r") as f:
            assert f.read()=="1"

