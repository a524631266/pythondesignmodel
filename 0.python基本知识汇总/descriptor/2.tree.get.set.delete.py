# https://docs.python.org/3.3/howto/descriptor.html?highlight=descriptor
# https://www.cnblogs.com/amou/p/9232013.html 描述符只针对特定属性的操作控制
# 而__getattribute__（实例访问所有属性之前） __getattr__（实例无法找到属性的时候最后调用的）
#  __setatt__（设置所有实例属性） __delattr__是对所有实例属性的通用控制
# 在学习代理模式的时候会提到　描述符　的概念，那么描述符具体是什么？
# 通过官网介绍发现，描述符并不是只提供一种花里胡哨的语法糖工具，而是深入理解python工作机制的
# 一种方式
# __getattribute__
# 只要一个对象（类或实例）定义了如下三个重载符，这个对象就被认为是描述符
# __get__ __set__ __delete__
# If any of those methods are defined for an object, it is said to be a descriptor.
# 它的作用是什么？
# 其实它的作用是重写了类属性的查找链顺序的行为（看0.descriptor1.py）
# 描述符的分类
# 1.数据描述符 也即是定义了 __get__ __set__的对象
# 2.非数据描述符 只定义了__get__的对象  
# 这两者的区别是，在获取实例（非类）属性的顺序方面的优先级 __getattribute__(访问属性、方法的主入口)判断是否含有__get__方法>数据描述符实例属性>__dict__实例属性>非数据描述符实例属性

# The important points to remember are: 见PropertyTest
# 1. descriptors are invoked by the __getattribute__() method
# 2. overriding __getattribute__() prevents automatic descriptor calls
# 3. object.__getattribute__() and type.__getattribute__() make different calls to __get__().
# 4. data descriptors always override instance dictionaries.
# 5. non-data descriptors may be overridden by instance dictionaries.

# threadlocal thireading.local()使用的场景
class DataDesc:
    def __init__(self):
        self.value = "Data"
        self.name = "a"
    def __get__(self,obj,type=None):# datadesc实例，属性所属实例，属性所属实例的类型
        print("DataDesc.__get__",type)
        print("obj",obj)
        return self.value
        # return 1 
    def __set__(self,obj,value):
        self.value = value

class NonDataDesc(object):
    def __init__(self):
        self.value = "NonData"
        self.name = "nn"
    def __get__(self,instance,owner):
        return self.value

class Container:
    data = DataDesc()
    nondata = NonDataDesc()
    # def __init__(self):
        # self.data = DataDesc()
        # self.nondata = NonDataDesc()
    def __getattribute__(self,key):
        """
            实例访问的时候调用，类不调用
        """
        print("主入口")
        # 也即是在查找__dict__中的属性方法前调用的，所以下面是无限循环
        # return self.__dict__[key] 
        return object.__getattribute__(self,key)
        # return 1 # 阻止描述符的执行，直接返回1
    def __getattr__(self,key):
        print("找不到key",key)

print("########################1.属性property########################")
# 描述符的特殊应用
# @property
class PropertyTest:
    def __init__(self,method):
        self.method = method
        self.methodname = method.__name__
    def __get__(self,obj,type):
        value = self.method(obj)
        #在第二次使用属性的时候立马调用，无需再走这个了
        setattr(obj,self.methodname,value)
        return value
        # return obj.__dict__[self.methodname]
    def __set__(self,obj,value):
        """
        在开启这个方法的时候，会覆盖实例的name
        在不开启是时候如果直接调用name只会提取"aaaaaaa"
        """
        pass
class A:
    def __init__(self):
        self._name = "zll"
        self.name = "aaaaaa"
    # @property 
    @PropertyTest
    def name(self):
        print("A　NAME 方法")
        return self._name
a = A()
print(a.name) 
print(a.name) 
print("########################2.函数与类方法########################")
# 其实函数与类方法是通过非数据描述符建立联系的
# 在充分理解描述符中的obj（调用该类的宿主对象实例）,type（宿主实例类型）的基础上
# 实际上类方法默认是以非数据描述符形式存在的

# class EquSay:
#     def __init__(self,name):
#         slef.name = name
#     def __get__(self,obj,objtype):
#         return types.MethodType(self, obj, objtype)

if __name__ == "__main__":
    c = Container()
    # c.nondata = NonDataDesc()
    print(c.data)
    print("22222222222222")  
    print(Container.nondata)  
    print("##################")
    c = DataDesc()
    print(c.__dict__)