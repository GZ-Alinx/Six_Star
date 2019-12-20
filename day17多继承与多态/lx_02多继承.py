#  可以继承多个父类


class A:
    def test(self):
        print('123')


class B:
    def demo(self):
        print('333')


class C(A, B):
    pass


c = C()
c.demo()
c.test()

