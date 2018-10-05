# 在python中作用域遵循 LEGB原则依次寻找变量所在域,如果没有,抛错

# 内置作用域为B 最最上层
import builtins

print(builtins is __builtin__)


def multiple(x,y):
    x = 2
    y = [3,4]
    print(id(x),id(y))
    return x,y

X = 1
L = [1,2]
X,L = multiple(X,L)
X,L
