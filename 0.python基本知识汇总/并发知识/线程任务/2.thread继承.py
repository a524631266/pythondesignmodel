from threading import Thread
import time
import os
class ThreadTask(Thread):
    def run(self):
        for x in [1,2,3]:
            time.sleep(1)
            print("my name is ",self.name,x,os.getpid(),end="\n\r")
def main():
    for i in [1,2,3]:
        t = ThreadTask()
        t.start()
    print("main pid",os.getpid())
if __name__ == '__main__':
    main()

    