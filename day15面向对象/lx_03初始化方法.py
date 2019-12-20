# __init__
"""
初始化方法
"""

# class Cat:
#     def __init__(self):
#         print("初始化方法")
#         self.name = 'Tom'
#
#     def eat(self):
#         print('8888888')
#
#     def bat(self):
#         print('%s' % self.name)
#
#
# tom = Cat()
# tom.bat()
#
# new_tom = Cat()
# new_tom.bat()


# 参数的方式 构造初始化
class new_Cat:
    def __init__(self, name):
        print("初始化方法")
        # self.属性 = 形参
        self.name = name

    def eat(self):
        print('8888888')

    def bat(self):
        print('%s' % self.name)


build_Cat = new_Cat('88888888888')   # 实例化的时候穿参
build_Cat.bat()
