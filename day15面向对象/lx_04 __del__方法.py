"""
del 方法
    程序运行需要在内存中开辟一个内存空间, 默认del也会执行
    在对象销毁之前，还希望对象再做一些事情
"""


class new_Cat:
    def __init__(self, name):
        print("初始化方法")
        # self.属性 = 形参
        self.name = name

    def __del__(self):
        print("%s 已销毁" % self.name)

    def eat(self):
        print('8888888')

    def bat(self):
        print('%s' % self.name)


build_Cat = new_Cat('88888888888')   # 实例化的时候穿参
build_Cat.bat()
print(build_Cat.name)


# 就算不写 也默认会销毁执行结束的程序