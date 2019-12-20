# 简单代码
def foo():
    print("foo")

# foo  # 表示函数
# foo()  # 表示函数调用


def demo():
    print("demo")


demo = lambda x: x+1
print(demo(3))


# 装饰器

def w1(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        return func()
    return inner


@w1  # python 中的一种语法糖
def f1():
    print('f1')

# @w1 相当于w1(f1)
"""
最后等于如下代码
def inner():
     # 验证1
     # 验证2
     # 验证3
     f1()   func 是参数， 此时func等于f1

这就是装饰器 
"""
# 产生背景: 开放封闭原则
"""
    规定已经实现的功能不允许被修改，但可以扩展
"""