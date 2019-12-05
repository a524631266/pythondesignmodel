# 单例模式，为什么要单例呢？
# 当项目中使用一些类，这些类是整个项目生命周期中只存在一份
# 比如，当你想写一个配置信息类（spring boot 中的envirements配置类）
# 在生命周期中只能存在一份，用来读取当前配置，后期修改配置信息的话另说
class Singleton:
    def foo(self):
        pass
single = Singleton()

