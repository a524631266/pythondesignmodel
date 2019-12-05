import threading
# 使用类模式 ,此时线程不安全
class SingletonCSafe(object):
    # 默认是是对object进行加锁的，所以需要没有必要传入其他对象，否则在
    # 多线程的情况下，无法保证加的是同一把锁
    lock = threading.Lock()
    def __init__(self, *args, **kwargs):
        import time
        time.sleep(1)
        pass
     
    # 加锁方式1 非double Check ,但是会出现性能问题，看到锁，必须要想到哪段代码耗时或出现问题
    @classmethod
    def instance(cls, *args, **kwargs):
        # 这里的 cls == SingletonC 
        # print(id(cls), id(SingletonC))
        # SingletonCSafe.lock.acquire()
        with SingletonCSafe.lock:
            if not hasattr(cls, "_instance"):
                cls._instance = cls(*args, **kwargs)
        # SingletonCSafe.lock.release()
        return cls._instance

    # 加锁方式2 double Check
    @classmethod
    def instance2(cls, *args, **kwargs):
        # 这里的 cls == SingletonC 
        # print(id(cls), id(SingletonC))
        print("SingletonCSafe.lock id:", id(SingletonCSafe.lock))
        if not hasattr(cls, "_instance"):
            SingletonCSafe.lock.acquire()
            if not hasattr(cls, "_instance"):
                print("init .....")
                cls._instance = cls(*args, **kwargs)
            SingletonCSafe.lock.release()
        return cls._instance

if __name__ == '__main__':
    def call1():
        a = SingletonCSafe.instance()
        print(id(a))
    thread1 = threading.Thread(target=call1)
    thread2 = threading.Thread(target=call1)
    thread1.start()
    thread2.start()