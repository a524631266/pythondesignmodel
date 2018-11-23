# GIL global interprate lock

# 线程是假的由于gil变量的存在,也就是说线程在同一时刻,只能有一个在跑
# 进程是么有GIL的
# 可以搞两个进程或者线程验证这个思想

# 解决锁的问题
gcc GILSolve.c -shared -o ***.so
使用 ctyps 里面的 crun = cdll.loadLibrary("***.so")
在 在Thread(target=crun)
就可以解决GIL问题了