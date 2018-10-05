
# repr 全精度显示 python2中
nm = 3.12159 * 2
# str 用户友好方式
class Num:
    def __init__(self,num):
        self.num = num 
    def __repr__(self):#  repr一般使用在交互模式中的显示,可以做细节处理
        
        return str(self.num+3)
    def __str__(cls): # str是一般打印结果
        return str(cls.num+1)
print(Num(2.34))

L = [None] * 100
print(type(L)) # python3  <class 'list'>
print(type(L) == list)


## continue operator
print(1<6>3<8)


## == 代表变量所引用的值是否相等
a = [1,2,3]
b = [1,2,3]
a == b #true
##　is 更加严格,代表是否是相同引用
a is b #false



a = 1
b = 2
c = 3
d = a + b \
    + c
print(d)


x = "a"
def p():
    x="b"
    print(x)
p()
print(x)


print(",".join(["1","2","3","4"]))