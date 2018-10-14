class addclass:
    # names = ["aaa"]
    def __init__(self,name):
        self.name = name
    def print(self):
        print(self.name)

def add(a,b):
    return a + b
# 使用type添加一个add2类 object.__new__(cls)
add2 = type("add2",(),{"name":"zhanglll"})
# 元类用来干什么? 元类是用来拦截并扩展 "类的创建" 类似装饰器功能


def main():
    # print(add.__class__.__class__) # <class 'type'>
    print(add2().name)
    print(add2.name)
    print(add2.__dict__)
    print(addclass.__dict__) # __dict__可以显示类的基本属性
    print("#############")
    a = addclass("name")
    print(addclass.print)
    a.print() 
    addclass.__dict__["names"].append(222)
    a.print()
if __name__ == '__main__':
    main()