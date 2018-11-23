# 看下threading.current_thread()就是用这个_active = {}
# _active[thread_id] = obj 
# 全局不能用,传参又费劲,用一个线程本地的存储会非常有效
# 其实质其实就是数据描述符 (同时修改了__get__ __set__)
# 定然是在
from threading import Thread,local
import time
globalname = local()

def getname():
    print(globalname.name) # 永远不会变成相同 的

def setname(name):
    globalname.name = name
    time.sleep(1)
    getname()

g = Thread(target = setname,args=("wang",))
g1 = Thread(target = setname,args=("li",))
g.start()
g1.start()