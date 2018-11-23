import os
import time
# 1.在fork前只打印一遍
print("1111111")

ret = os.fork()

if ret > 0:
    print("父亲进程in")
    time.sleep(3)
    print("父亲进程out")
else:
    print("子进程in")
    time.sleep(5)
    #　2.父进程结束之后仍然会执行子进程
    print("子进程out")

# 3.根据2可以判断,这里会打印两遍
print("----over -----")