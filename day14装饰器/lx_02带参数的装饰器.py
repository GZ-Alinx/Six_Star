# 带参数的装饰器
"""
 产生背景：
   1. 被装饰的函数需要参数调用  本文为 foo 函数
   2. 新代码需要参数调用  本文为 timefunc 函数
"""


# 新代码
from time import ctime


def timefunc(func):
    def run(a, b):
        print(a, b)
        func(a, b)
    return run

# 旧代码
@timefunc
def foo(a, b):
    print(a + b)


if __name__ == '__main__':
    print(foo(1, 2), ctime())