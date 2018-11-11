# https://www.cnblogs.com/wongbingming/p/8973859.html
# type 三参数

class BaseClass:
    def talk(self):
        print("my is baseClass")

def say(self):
    print("asdd",self.name)

#  动态创建类 
# 什么是类？可能谁都知道，类就是用来创建对象的「模板」。
# 那什么是元类呢？一句话通俗来说，元类就是创建类（class）的「模板」（type）。
# 为什么type能用来创建类？因为它本身是一个元类。使用元类创建类，那就合理了
User = type("User1",(BaseClass,),{"name":"zhangll","say":say})
# type如果只传一个参数就是检测对象的类型，　实例的类型是类，类的类型都是type
def main():
    user = User()
    user.say() # asdd zhangll
    print(User.__name__) # User1

if __name__ == '__main__':
    main()
