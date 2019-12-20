"""
str 方法

"""


class new_Cat:
    def __init__(self, name):
        # print("初始化方法")
        # self.属性 = 形参
        self.name = name

    def __str__(self):
        # 如果直接执行类，会得到一串16进制内存地址，那么我们可以自定义这个返回值
        # str 方法必须返回一个字符串
        return "我是监控数据类 %s" % self.name


build_Cat = new_Cat('88888888888')  # 实例化的时候穿参

# 调用的时候  友好的返回 而在也不是16进制的内存地址
print(build_Cat)
