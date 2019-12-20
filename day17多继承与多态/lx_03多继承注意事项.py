# 多继承注意事项


# 相同的方法函数  怎么调用
class A:
    def test(self):
        print('a-123')

    def demo(self):
        print('a-333')


class B:
    def demo(self):
        print('b-333')

    def test(self):
        print('b-123')


class C(A, B):
    pass


# 如果有相同的方法会调用A的方法
c = C()
c.demo()
c.test()

# 使用下面的方法查看方法的搜索顺序
# 使用类名.
print(C.__mro__)

"""
class 'object' 解释
    class 'object' 是为所有的对象提供的基类
    py3中定义类后没有指定父类会默认调用object作为基类
    为了让代码能在py2.x 和py3.x中运行  需要在类中写上object关键字
    例子：
        class B(object):
"""
