class A(object):
    def __init__(self):
        self.num1 = 1
        self.num2 = 2


class C(object):
    def __init__(self):
        self.num3 = 4


class B(A, C):
    def demo(self):
        print(self.num2)
        print(self.num1)


# 先调的先使用，不能永初复的方法 包括初始化方法
b = B()
b.demo()