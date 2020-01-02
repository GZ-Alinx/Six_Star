import threading
from threading import Thread
import time

num = 0


def work1(n):
    global num
    for i in range(n):
        mutex.acquire()  # 上锁
        num += 1
        mutex.release()  # 解锁
    print("work1 num：", num)


def work2(n):
    global num
    for i in range(n):
        mutex.acquire()
        num += 1
        mutex.release()
    print("work2 num：", num)


mutex = threading.Lock()  # 因为资源竞争，所以需要上锁
print('创建前，num的值：', num)

t1 = Thread(target=work1, args=(100000,))
t1.start()
print()
t2 = Thread(target=work2, args=(100000,))
t2.start()