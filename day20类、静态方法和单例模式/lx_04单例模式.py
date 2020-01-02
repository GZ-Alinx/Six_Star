# 单例模式：  单一的一个例子
# 通过这个类创建出的对象 不管多少个内存地址都是相同的
# 参数的方式 构造初始化


class new_Cat(object):
    instance = None
    init_flag = False

    def __init__(self):
        if new_Cat.init_flag:
            print("初始化")
            new_Cat.init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


p1 = new_Cat()
p2 = new_Cat()
# 内存地址相同
print(p1)
print(p2)
