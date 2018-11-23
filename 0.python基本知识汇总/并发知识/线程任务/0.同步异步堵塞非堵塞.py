# 堵塞 非堵塞是程序是否要等,堵塞不耗费资源
# 同步 为程序执行的确定性,有规律的,即按照正常步调往下走
# 一般 为程序不确定性

# 异步代码准确理解
from multiprocessing import Pool
import os
import time 
def childrendo():
    print("-----子进程",os.getpid(),os.getppid())
    time.sleep(3)
    return "好好"
def fatherdo(args):
    print("-----其实是父进程",os.getpid(),args)

pool = Pool(3)
pool.apply_async(func=childrendo,callback=fatherdo)


time.sleep(5)#父进程在等待的过程中,忽然收到通知要执行callback了,多么直接干脆
print("____farter___",os.getpid())

# while True:
#     time.sleep(1)
#     print("fahter",os.getpid())
