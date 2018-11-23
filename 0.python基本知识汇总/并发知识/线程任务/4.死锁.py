#  死锁的其中一个环节就是打结,交叉 或者更一般意义上来讲就是
# 两人吵架,每个人都再等另一半道歉,然后无限循环,就gameover了
# 程序来讲,首先要有两个人各拿着对另一半的想法(等你先道歉)
from threading import Thread,Lock,current_thread
import time
manthinklock = Lock()

womanthinklock = Lock()
class manwaitforwomanapology(Thread):
    def run(self):
        n = manthinklock.acquire()
        print(self.name,"正常情况下,在取锁的时候为true",n)
        time.sleep(1)
        if womanthinklock.acquire(timeout=1):
            print(self.name,"解锁成功")
        else:
            print(self.name,"没解锁成功")
        manthinklock.release()
class womanwaitformanaplogy(Thread):
    def run(self):
        n = womanthinklock.acquire()
        print(self.name,"正常情况下,在取锁的时候为true",n)
        time.sleep(1)
        if manthinklock.acquire(timeout=2):
            print(self.name,"解锁成功")
        else:
            print(self.name,"没解锁成功")
        womanthinklock.release()

t1 = manwaitforwomanapology()
t2 = womanwaitformanaplogy()
t1.start()
t2.start()


#解决办法1 加上timeout
# 第二种为银行家算法,主要思想是先满足部分用户,接下来通过上一期的还款取得的钱贷给其他人....
# 一般情况下会遇到死锁


def m():
    print(current_thread().name,1)
for i in range(5):
    t = Thread(target=m)
    t.start()