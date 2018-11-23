# 类似于 multiprocessing
from threading import Thread
import os
import time
l = [1,2,3]

# 特点1，线程的pid与主程序的pid一样，说明，线程是由进程创建的
def test():
    time.sleep(1)
    l.append(1)
    print("线程",os.getpid())

for i in range(5):
    t = Thread(target=test)
    t.start()#只有start之后才能开始执行
    # t.join() # 进程会等待，等到test执行完，才会执行main，否则会执行main并等待线程执行完成退出程序
# 特点2，这里只打印一句，说明，线程只执行test代码段
print("main",os.getpid())
print(l)