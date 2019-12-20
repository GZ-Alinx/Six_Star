# 私有属性 与 私有方法
# python 对变量做的特殊处理


class Girl:
    def __init__(self, name):
        self.name = name
        self.__age = 18  # 私有属性

    def __secret(self):  # 私有方法
        print('年龄：', self.__age)


# 私有属性与私有方法在外部都是不能直接调用的
xm = Girl('xiaomei')
print(xm.name)
# print(xm.__age)


# 实际上是伪私有  如果想要调用 还是可以的
print(xm._Girl__age)  # 私有属性调用
xm._Girl__secret()  # 私有方法调用
