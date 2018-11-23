from threading import Thread,Lock
# 线程的特点与进程的区别是,线程可以在一份代码块中共享变量,而进程fork一般是各自一份
num = 0
lock = Lock() 
#互斥锁,其唯一目的是多个线程对同一资源产生竞争的时候使用,为通知形式[sleep -> 发消息],非轮询(for/while true)[耗cpu]
# 如果没有锁,那么程序具有不确定性,因为在num = num+1 会执行2步骤,一步是求和,一步是赋值
def read100():
    global num
    # global lock
    lock.acquire()#1.放在for循环外面
    for i in range(1000000):
        # lock.acquire()#2.放在for循环里面
        num += 1
        # lock.release()#里面   
    lock.release()
    print("--------",num)

t = Thread(target=read100)
t2 = Thread(target=read100)
t.start()
t2.start()