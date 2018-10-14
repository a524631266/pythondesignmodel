def say(a,*b,c):
    print(a,*b,c)
#  这里的* 代表的一个占位,不传任何参数,因为其后面没有参数表示,只表示,其后面的参数
#  均需要关键字表示,且 b c 可以互换,没有次序问题
def say2(a,*,b="b",c,d="e"):
    print(a,b,c,d)

def process(*args,notify=False):
    print(args,notify)

def main():
    say(1,2,c= 4)
    say(1,2,1,2,c=2)
    say2(1,c="a")

    process(123,4,5,notify =True)

    data = {"a":"a"}
    print(data.pop("a","cc"))
    print(data)


if __name__ == '__main__':
    main()