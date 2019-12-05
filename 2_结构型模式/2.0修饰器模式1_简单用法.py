# 修饰器模式主要的功能是用来扩展模块／功能
# 一般来说,这类功能/模块在软件上来说更偏向于 横切面关注点(cross-cutting concerns))
#　这类横切面关注点在数学上来书就像一个球的切面（只有一个点与球相交），故此得名
# 在软件方面就是每个模块(module)都可能需要拥有的通用性功能
#  1. 日志
#  2. 监控
#　３．缓存
#  4. 数据校验(验证密码 cookie)
#  5. 调试 webpack
#  6. 压缩
#  7. 解密
# 其用意是不修改其他对象的基础上进行功能的扩展
# 在python中主要是 @ 方法 扩展

def method2(func):
    """
        the method must do the follow two things :
         1. the input of the method should be a function which you want to warp
         2. the output of the method should be the function 

        if you want to do something else ,you can create a function that you want
        to execute 
    """
    def warpper():
        print("11111111111")
        return func
    return warpper()

class A(object):
    def __init__(self,name):
        # pass
        self.name = name
    @method2
    def say(self):
        print("my name is {} ".format(self.name))

#


def main():
    a= A("zhangll")
    a.say()

if __name__ == '__main__':
    main()