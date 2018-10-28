# __dict__ 每个对象（实例，类，元类）具有的属性
# 可以理解为各个对象命名空间存在的变量
# https://www.cnblogs.com/Jimmy1988/p/6808237.html
# 1. 访问顺序
# 对象 => 类 => 父类 =>__getattr__
# 2. 赋值
# 对象赋值就修改对象的，类赋值修改类的，依次类推
#　本身的作用域中修改　不管后期如何修改，井水不犯河水
class BaseClass(object):
    testpoolb = [9,0]
    pass
    # def __new__(cls,name,bases,attrs):
    #     return super().__new__(cls,name,bases,attrs)

class Test(BaseClass):
    testpool = [1,2,3]
    def __init__(self):
        self.testpool2 = [0,1]

def main():
    t = Test()
    print(t.__dict__) # {'testpool2': [0, 1]}
    print(t.testpool) # 对象 => 类
    print(t.testpoolb)

    t.testpool = [1,1,1] # 只修改了实例内的testpool ，没有修改类的属性
    print(t.__dict__)# {'testpool2': [0, 1], 'testpool': [1, 1, 1]}
    print(Test.testpool) # 1,2,3

if __name__ == '__main__':
    main()
