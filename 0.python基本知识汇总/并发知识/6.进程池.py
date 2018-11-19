# 池子是一个缓存区,
# 好比干一件事情,不是一杆到底,而是分几步骤,有个缓冲区,用来完成一部分功能
# 特点1.向池子中加任务,任务均是由子进程完成,可以观察pid是否一致
# 2.池子必须要有两步操作,close和join
from multiprocessing import Pool
import os
import time
def work(a):
    for i in range(2):
        time.sleep(1)
        print("此时的任务都是子进程pid",os.getpid(),a,i)

#1.创建3个池子
pool  = Pool(3) # 多少个池子好呢?一般进过成本分析得到,比如压力测试,资源最大化..
print("主进程",os.getpid())
for i in range(10):
    print("看看是否会堵塞,当我们创建10个任务的时候")
    # time.sleep(1)
    pool.apply_async(work,(i,))#一旦应用就会执行,且等待work函数执行完全之后才释放池子位置

pool.close()#此时代表关闭池子的入口,不能再往池子中加水了,否则报错
pool.join()# 主进程等待池子中的进程结束,否则,直接父进程结束之后,池子就挂了

print("主进程",os.getpid())