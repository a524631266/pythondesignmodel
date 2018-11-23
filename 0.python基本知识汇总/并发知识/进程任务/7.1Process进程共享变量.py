# 进程正常来说是一个拥有独立空间的程序
# 要想实现进程之间的通信,应该拥有一个可以跟进程进行交互的管道
# 1.Process 中进行交互的队列,先进先出,打气筒
from multiprocessing import Queue,Process
import os
import time
q = Queue()
print("main pid",os.getpid())
def test(q):
    print("____",os.getpid())
    for i in range(10):
        print("__insert",i)
        q.put(i)

        time.sleep(1)
def getTest(q):
    print("______get",os.getpid())
    while True:
        data = q.get()# 一直等待
        # data = q.get_nowait() # 立马报错所以如果用nowait需要捕获异常
        print("get_",data)
p = Process(target=test,args=(q,))#开启一个子进程
p2 = Process(target=getTest,args=(q,))# 开启第二个子进程
p.start()
# p.join() # join这一步是main主进程在此句等待,所以,会先执行玩test之后,才能往下
p2.start()
# 由于线程q.get是堵塞状态,因此程序不会退出到terminal