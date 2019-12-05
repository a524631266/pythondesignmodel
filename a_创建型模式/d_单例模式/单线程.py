# 单例模式，为什么要单例呢？ 下面是线程不安全的应用
# 当项目中使用一些类，这些类是整个项目生命周期中只存在一份
# 比如，当你想写一个配置信息类（spring boot 中的envirements配置类）
# 在生命周期中只能存在一份，用来读取当前配置，后期修改配置信息的话另说
# 最简单的直接生成一个模板single，但是在 导入的时候还是会出现线程不安全
class Singleton:
    def foo(self):
        pass
single = Singleton()

# 使用装饰器 导入的时候还是会出现线程不安全
def SingletonDesc(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

@SingletonDesc
class SingletonD(object):
    a = 1
    def __init__(self, x = 0):
        self.x = x
# 方法 1 控制为单例模式 a1与 a2是同一个对象
# a1 = SingletonD(2)
# a2 = SingletonD(3)
# print("a1:", id(a1) , ",a1.x:", a1.x, "\n::a2" , id(a2), ", a2.x", a2.x)

# 使用类模式 ,此时线程不安全
class SingletonC:
    def __init__(self, *args, **kwargs):
        import time
        time.sleep(1)
        pass
    @classmethod
    def instance(cls, *args, **kwargs):
        # print("object:    ",id(object), id(object))
        # 这里的 cls == SingletonC 
        # print("cls:    ",id(cls), id(SingletonC))
        if not hasattr(cls, "_instance"):
            cls._instance = cls(*args, **kwargs)
        return cls._instance


