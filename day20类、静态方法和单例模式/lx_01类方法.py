# 类方法
# @classmethod


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

tool1 = Tool('123')
tool2 = Tool('1234')
Tool.show_tool()