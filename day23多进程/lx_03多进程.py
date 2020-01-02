import multiprocessing
from multiprocessing import Process
import time



def work1():
    "子进程执行"
    while True:
        print('--1--')
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=work1)
    p.start()
    while True:
        print('--2--')
        time.sleep(1)