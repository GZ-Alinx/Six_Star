import os
from multiprocessing import Process
from time import sleep




def work(name, age, **kwargs):
    for i in range(10):
        print("子进程， name=%s, age=%d,pid=%d"% (name, age, os.getpid()))
        print(kwargs)
        sleep(0.2)


if __name__ == '__main__':
    p = Process(target=work, args=('alinx', 26), kwargs={'m': '安德发撒旦发生地方'})
    p.start()
    p.join(0.5)  # 是否等待子进程执行结束, 或者等待多少秒
    p.terminate() # 不管子进程是否我完成，立即终止进程

