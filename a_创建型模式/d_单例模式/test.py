# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:05:39 2019
 
 获取属性的方法用来
@author: zhangll
"""


import threading
# from pythondesignmodel import 1_创建型模式
if __name__ == "__main__":

    # print(__file__)
    def callprintSingle():
        # 在多线程内部进行内部实时导入，会出现线程不安全情况
        from 单线程 import single,SingletonD,SingletonC
        from 多线程安全 import SingletonCSafe
        # print("单线程单例与装饰类 ",id(single), id(SingletonD(2)))
        # print("单线程 静态类: ", id(SingletonC.instance()))
        print("多线程 静态类加锁", id(SingletonCSafe.instance2()))
        pass
    thread1 = threading.Thread(name = "1", target= callprintSingle)
    thread2 = threading.Thread(name = "2", target= callprintSingle)
    thread1.start()
    thread2.start()

