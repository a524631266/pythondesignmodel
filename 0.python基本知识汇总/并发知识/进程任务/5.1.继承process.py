# 创建process子类
import time
from multiprocessing import Process

class MyProcess(Process):# 继承Process
    def __init__(self,interval=1):
        Process.__init__(self)# 给对象附加一个拥有process实例的初识化实例
        self.interval = interval
    def run(self):
        starttime = time.time()
        print("waiting for seconde...")
        time.sleep(self.interval)
        print("take %08f s"%(time.time()-starttime))
if __name__ == "__main__":
    p = MyProcess(4)
    # print(p.__dict__)
    p.start()
    