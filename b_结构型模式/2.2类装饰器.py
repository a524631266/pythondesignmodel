import functools
# 在使用类作为装饰器时,需要用到__call__方法
# __call__方法是在实例(非类)打call的时候用的
# 这里的打call就是
# a = A()
# a() 实例打call

# 如下是一个打电话的对话,A为一个固定电话用户  
class A(object):
    def __init__(self,name):
        self.name = name
    def __call__(self,func):
        @functools.wraps(func)
        def warp(*args):
            self.doSomething()
            return func(*args)
        return warp
    def doSomething(self):
        print(self.name)

@A("This is zhangll, who is that?")
def sayHello(callname):
    print("Hello this is  :",callname)

def main():
    sayHello("jianglina")

if __name__ == '__main__':
    main()