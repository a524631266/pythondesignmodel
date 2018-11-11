# descriptor 描述符(描述器)的概念
# 1.某个东西的具体描述,比如 人是什么什么
# 在程序中代表了 A.X= 。。。
# 所以一般更对象属性的相关操作有关，比如
#  __get__ __set__ __del__
# 2.官方说法，是一个对象属性，同时这个属性拥有一系列bind behavior
# 在类属性的查找链顺序
# 比如找ao是类a的实例，ao.poolb寻找路径
# 1.先找ao实例中的是否存在属性poolb，如下看到，ａｏ实例空间中只有ｎａｍｅ
# 2.再查找type(ao) == ao.__class__这个是ａｏ所属的类空间上的属性，可以发现
# ａｏ的所属类为ａ(B)类，而其只有poola属性，所以依旧要向ａ所继承的父类中找
# 3.通过父类Ｂ中的属性查找到
# ４.如果在所有类中无法找到，就会查找所有类(class)的类型(type)【不包含元类】，
# 其实在py3中class是type的实例，
class B(object):
    poolb = [1,2,3]


class a(B):
    """
        a是一个类，包含一个ｐｏｏｌａ属性
    """
    poola = [1,2,3,4]
    def __init__(self):
        self.name = 1

def main():
    # 类对象中有pool属性，还有弱引用 weakref
    print(a.__dict__)
    print(a.poolb)# 先找a类中的__dict__ 然后找它的父类中的dict
    #  查看 a类的类型的两种方式
    print(type(a))
    print(a.__class__)
    # a的实例
    print("######################")
    ao = a()
    print(ao.__dict__) #{name:1}
    print(type(ao).__dict__)
    print("######################")
    print(type(int))
    print(isinstance(a,B))
if __name__ == '__main__':
    main()
