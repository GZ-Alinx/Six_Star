import os
from multiprocessing import Process
import time


def work1():
    "子进程执行"
    while True:
        print('子进程PID：', os.getpid())
        print('--1--')
        time.sleep(1)


if __name__ == '__main__':
    print('父进程PID：', os.getpid())
    p = Process(target=work1)
    p.start()
    while True:
        print('父进程PID：', os.getpid())
        print('--2--')
        time.sleep(1)
        print('-' * 20)
