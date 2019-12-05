# 场景是两个操作速度不同步的时候,就用这个模式来作为缓冲
# 可以说是一个解耦的操作,一坨乱码,是不能理喻的,需要理清每个部分,会不会影响升级
# 需要持续看代码写得好的人看

# 实际应用场景,爬虫的爬取,以及爬虫对数据的处理,分布式爬虫
# 这里用Queue 不是process和thread中的q,而是queue里面的Queue redis
from threading import Thread
from queue import Queue
import time
q = Queue()
class Producer(Thread):
    def run(self):
        # global q
        # global q
        while True:
            for i in range(5):
                q.put("name"+str(i))
            time.sleep(1)


class Consumer(Thread):
    def run(self):
        # global q
        while True:
            for i in range(2):
                print(self.name,"消费者",q.get())
            time.sleep(1)


p = Producer()
c = Consumer()
p.start()
c.start()