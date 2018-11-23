import os
import time
g_num = 100

ret = os.fork()

if ret > 0:
    g_num += 1
    time.sleep(1)
    print("father num",g_num) # 101
else:
    time.sleep(3)
    print("children num",g_num) # 100
# 说明 父子进程虽然公用一份代码,但是,变量是在不同空间的

# 如何共享????? 进程通信

