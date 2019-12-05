# 首先了解 原型的出现的作用
# 在js中,每个函数,都是一个对象,同时每个对象都有一条链,这条链的源头
# 都是所有这个方法所生成的对象所共有的,不管这条链是不是在创建对象之后
# 加入的,对象都可以引用

# 在python中,原型链所涉及的是对象的生成 有两种,有两种方式
## 1. 引用(浅拷贝) reference   copy.copy
## 2. 深拷贝 deep copy   copy.deepcopy()
# ##　在python中很多应用都涉及到原型设计,但是都不会显式地叫原型模式,
# 因为对象的clone是 python语言的一种特性
# 
 

# __dict__.update

class A(object):
    names = "asd"
    def __init__(self,name,age,**rest):
        self.name = name
        self.age = age
        print(rest)
        self.__dict__.update(rest)
        print(self.names)

def main():
    pass

if __name__ == '__main__':
    a = {"name":"zhang","age":90}
    print(id(a))
    a.update({"na":"333"})
    print(id(a))