# 外观(facade)模式 主要是针对复杂系统的简单封装
# 为哈要简单封装,由于一般系统会变得越发复杂,模块与模块
# 实例与实例等等的交互使得系统变得非常复杂,而有时候复杂
# 系统不需要给客户端暴露复杂的内部,而通过facade可以很好
# 地隐藏系统内部的复杂性,而只需要暴露核心(简单)的接口
# 例子
# 1.电脑启动 启动按钮,封装了各种软硬件启动的必备流程
# 1.1 minix3系统,通过
# 2.汽车启动 钥匙开启的接口
# 3.服务启动 tomcat start.sh文件
# 4.客户与公司交流的客服途径(客服充当的外观角色) 想起了滴滴事件..客服还是外包的..这样很容易出现问题
# 总得来说,一键启动,轻松搞定事情的收尾工作一般可以提供一个外观接口

## 尝试构造一个操作系统
##　类似于minix3   
# 模块化的操作系统可以有很多有意思的服务进程,包括文件服务进程、进程服务进程、
# 身份验证服务进程、网络服务进程和图形/窗口服务进程
from enum import Enum
from abc import abstractmethod,ABCMeta
State = Enum("State","new running sleeping restart zombie")

# print(State.__dict__)

class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        # print(111)
        pass
    def __str__(self):
        return self.name
    @abstractmethod
    def boot(self):
        pass 
    @abstractmethod
    def kill(self,restart = True):
        pass
class FileServer(Server):
    """
        文件系统服务类,可以添加创建文件
        :param Server: 
    """
    def __init__(self):
        self.name = "FileServer"
        self.state = State.new
    def boot(self):
        print("启动 {}".format(self))
    def kill(self,restart = True):
        print("终止服务 {}".format(self))
        self.state = State.restart if restart else State.zombie
    def create_file(self,user,filename,permissions):
        print("试着给{}创建一个拥有权限{}的文件 {}".format(user,permissions,filename))

class ProcessServer(Server):
    """
        进程管理服务类 这里多了一个创建进程的细节
        :param Server: 
    """
    def __init__(self):
        self.name = "ProcessServer"
        self.state = State.new
    def boot(self):
        print("启动 {}".format(self))
    def kill(self,restart = True):
        print("终止服务 {}".format(self))
        self.state = State.restart if restart else State.zombie
    def create_process(self, user, name):
        '''检查用户权限和生成PID等'''
        print("trying to create the process '{}' for user '{}'".format(name, user))


## 练习
class NetWorkServer(Server):
    def __init__(self):
        self.name = "网络服务"
        self.state = State.new
    def boot(self):
        print("启动 {}".format(self))
    def kill(self,restart = True):
        print("终止服务 {}".format(self))
        self.state = State.restart if restart else State.zombie
    def ping(self,ip:str):
        print("{}开始尝试链接网络{}".format(self,ip))

class OpServer(object):
    """
        创建一个外观类,用来统一管理服务与接口
    """
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()
        self.nw = NetWorkServer()
        self.start()
    def start(self):
        [i.boot() for i in (self.fs,self.ps,self.nw)]
    def create_file(self,user,filename,permissions):
        self.fs.create_file(user,filename,permissions)
    def create_process(self, user, name):
        self.ps.create_process(user,name)
    def ping(self,ip):
        self.nw.ping(ip)


def main():
    ops = OpServer()
    ops.create_file("zhangll","op","666")
    ops.create_process("zhangll","django")
    ops.ping("192.168.10.1")
if __name__ == '__main__':
    main()