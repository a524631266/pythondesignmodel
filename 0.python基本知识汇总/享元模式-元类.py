
def add(a,b):
    return a + b
# 使用type添加一个add2类
add2 = type("add2",(),{"name":"zhanglll"})

def main():
    # print(add.__class__.__class__) # <class 'type'>
    print(add2().name)
    print(add2.name)
    print("111")
if __name__ == '__main__':
    main()