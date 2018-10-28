# descriptor 描述符(描述器)的概念
# 1.某个东西的具体描述,比如 人是什么什么
# 在程序中代表了 A.X= 。。。
# 所以一般更对象属性的相关操作有关，比如
#  __get__ __set__ __del__
# 2.官方说法，是一个对象属性，同时这个属性拥有一系列bind behavior

class B(object):
    poolb = [1,2,3]


class a(B):
    poola = [1,2,3,4]

def main():
    # 类对象中有pool属性，还有弱引用 weakref
    print(a.__dict__)
    print(a.poolb)# 先找a类中的__dict__ 然后找
    #  查看 a类的类型的两种方式
    print(type(a))
    print(a.__class__)
    # 
    print(type(int))
    print(isinstance(a,B))
if __name__ == '__main__':
    main()
