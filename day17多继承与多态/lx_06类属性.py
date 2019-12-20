class Tool(object):
    # 定义类属性
    count = 0

    def __init__(self, name):
        self.name = name
        self.count = "123"
        Tool.count += 1


tool1 = Tool('123')
tool2 = Tool('abc')
tool3 = Tool('..,/!@#')
print(tool1, tool2, tool3)


print("%s 个工具" % Tool.count)  # 类属性就使用类. 调用
print("%s 个工具" % tool1.count)  # 实例属性使用实例. 调用
#  区分调用方式  否则调用的数据不准确