import a
import b
a.a = 20
print(a.a) # 20
print(b.b) # 10 修改模块的变量不会改变

a.alist[2] =2000
print(a.alist) # 2000
print(b.blist) # 2000 但是会同步改变





