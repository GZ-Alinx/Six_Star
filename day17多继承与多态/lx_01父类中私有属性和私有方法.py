# 继承中： 私有方法，私有属性调用问题
class A:
    def __init__(self):
        self.name = 10
        self.__num2 = 20

    def __test(self):
        print("私有: {}{}".format(self.name, self.__num2))

    def test(self):
        print(self.__num2)


class B(A):
    def demo(self):
        print(self.name)
        # 在子类的对象中，不能访问父类的私有属性和私有方法
        # print(self.__num2)
        # 如果确实想使用私有属性，私有方法
        print(self.test())


b = B()
b.demo()