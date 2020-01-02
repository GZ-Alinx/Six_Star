# 在一个实例中不需要访问类属性，也不需要访问实例方法，“这样的方法叫做静态方法”
# 静态方法也需使用到装饰器


class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    # 实例方法第一个必须是self
    @classmethod   # 类方法就是cls 可以不是cls 但约定是cls
    def show_tool(cls):
        """
        显示工具对象的总数
        :return:
        """
        print("工具对象的总数为", cls.count)

    @staticmethod
    def show_me(self):  # 看方法名虚线 提示可能是静态方法
        print("这是一个创建工具的类")


tool1 = Tool('123')
tool2 = Tool('1234')
Tool.show_tool()
print(tool2)