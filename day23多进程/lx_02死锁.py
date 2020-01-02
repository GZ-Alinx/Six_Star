import threading
import time



"""
锁的概念：

        当对全局资源存在写操作时，如果不能保证写入过程的原子性，会出现脏读脏写的情况，即线程不安全。
        Python的GIL只能保证原子操作的线程安全，因此在多线程编程时我们需要通过加锁来保证线程安全。
        最简单的锁是互斥锁（同步锁），互斥锁是用来解决io密集型场景产生的计算错误，即目的是为了
    保护共享的数据，同一时间只能有一个线程来修改共享的数据。

"""


# 在两个线程中，都想获取对方的锁，然后造成死锁的状态
class Mythread1(threading.Thread):

    def run(self):
        mutexA.acquire()  # 对A上锁
        # 等待1秒，等待另外一个线程上锁
        print('1中A上锁')
        time.sleep(1)
        mutexB.acquire()  # B上锁
        print('1中获取B的锁')
        mutexB.release()  # B解锁
        mutexB.release()  # 对A解锁


class Mythread2(threading.Thread):

    def run(self):
        mutexB.acquire()
        print('2中B上锁')
        time.sleep(1)
        mutexA.acquire()
        print('2中获取A的锁')
        mutexA.release()
        mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()


if __name__ == '__main__':
    t1 = Mythread1()
    t2 = Mythread2()
    t1.start()
    t2.start()


# 如何解决死锁?
"""
银行家算法：
    根据时间差去调用资源，完成任务

"""