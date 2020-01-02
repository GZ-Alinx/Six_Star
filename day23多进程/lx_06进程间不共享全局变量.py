from multiprocessing import Process
import os
import time


nums = [1, 2]


def work1():
    print("子进程1中PID=%d, nums=%s" % (os.getpid(), nums))


def work2():
    print("子进程2中PID=%d, nums=%s" % (os.getpid(), nums))


if __name__ == '__main__':
    p1 = Process(target=work1)
    p1.start()
    p1.join()

    p2 = Process(target=work2)
    p2.start()



"""
进程是系统进行资源分配的一个独立单位
线程是进程的实体，是CPU调度和分配的基本单位

区别：

一个程序至少拥有一个进程，一个进程至少有一个线程
线程的划分尺度小于进程（用到的资源比进程少）
进程在执行中拥有独立的内存单元
线程不能独立运行，必须依村在进程中

优缺点：

线程开销小，不利于资源的管理和保护，进程相反
"""