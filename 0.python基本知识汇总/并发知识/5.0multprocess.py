# fork只能用在linux
import time

from  multiprocessing import Process

def test(a):
    for i in range(10):
        time.sleep(1)
        print("-------test---------",a)
        # if i > 5:
        #     p.terminate()
p = Process(target=test,args=(1,))
p.start()

print("11111")
# 3秒之后马上停止,应用场景,timeout 比如超时之后干死
time.sleep(3)
p.terminate()
# 结束之后主进程不关闭,因为不能在termial中输入命令
p.join() # 只有在进程对象内完成了所有操作才能释放锁,主进程在等待堵塞
print("22222222222")
