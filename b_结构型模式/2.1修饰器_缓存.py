from timeit import Timer
import functools
#  timeit 官网　https://docs.python.org/3/library/timeit.html
# timeit 默认模式为10000次

# 可以发现 在不经过 性能优化的情况下,简单的循环递归非常缓慢
# 例子有两种
# 1. 斐波那契数列,这个是最基本的构造 循环递归自己,使用栈压入参数/返回值/局部变量等等,易发生内存泄露
# 但是能够做 只能并不是最优的(为啥不会会生成中间结果呢?如果是一棵树,程序是根节点,那么在根节点还没有计算完的情况下
# 子节点保留这对子节点的引用)
# 2. 求和序列,这个通过递归循环,同时也需要用到递归自己,但是耗内存,生成中间没用的变量 return 值


# 通过在middlestore上再嵌套一层用来控制是否使用缓存
def openwarp(usewarp=False):
    def warpping(middfunc):
        # usewarp = False
        # print("11111111111")    
        def warpper(func):
            if usewarp:
                return middfunc(func)
            else:
                return func
        return warpper
    return warpping
# 通过缓存来保持返回的结果
# 要点是需要返回缓存的结果,同时不再对缓存结果进行赋值,确保数据不再叠加运算


@openwarp(True)
def middlestore(func):
    result = {} # 第一次调用的时候产生
    # usewarp  = True # 在 装饰器上加一层 是否使用warpper的变量
    # fbnaci.__doc__ fubnaci.__name__ 重新返回原来的元素,因此需要包装一层
    # ('__module__', '__name__', '__qualname__', '__doc__','__annotations__')
    # 官方 https://docs.python.org/3.3/library/functools.html
    @functools.wraps(func)
    def warpper(*args):
        """
            该函数用来生成中间缓存2
        """
        # print(result)
        # print("func",func)
        if args not in result:
            result[args] = func(*args)
        return result[args]
    return warpper
    # else:
    #     return func



@middlestore
def fbnaci(n):
    """
     斐波那契序列，不包装　运行fbnaci(7)需要耗时7.9秒
    """
    assert n>=0,"列表数小于0"
    if n in [0,1]:
        return n
    else:
        return fbnaci(n-1)+fbnaci(n-2)

@middlestore
def sumbefore(n):
    """
     求和
    """
    return n if n == 0 else n + sumbefore(n-1)


def main():
    # 方法一 导入fbnaci包
    # t = Timer("fbnaci(7)","from __main__ import fbnaci")
    # 方法二 导入全部变量,包含fbnaci
    print("name,",fbnaci.__name__)
    print("name,",fbnaci.__doc__)
    t = Timer("fbnaci(7)",globals=globals())
    print(t.timeit(number=1000000)) # 7.5 s 每次循环
    t1 = Timer("sumbefore(7)",globals=globals()) 
    print(t1.timeit(number=1000000)) # 1.4 s 每次循环


## 当然,你可以使用尾递归来处理普通递归的在堆栈上的性能问题
# 尾递归的核心概念是在函数上使用上一层的结果作为下一层结果的相关输入用来存储中间变量
if __name__ == '__main__':
    main()