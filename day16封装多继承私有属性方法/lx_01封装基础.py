# 把特定的功能模块封装为一个整体 然后调用 就是类 对象了。。


# 需求
"""
 小明70公斤
 跑跑步会减0.5公斤
 名词吃东西增加1公斤
"""
# 以下就是一个封装的过程


class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        """
        跑步
        :return: 跑步
        """
        print("%s 爱跑步，跑步锻炼身体"% self.name)
        self.weight -= 0.5

    def eat(self):
        """
        吃东西
        :return: 吃东西
        """
        print("%s是个吃货" % self.name)
        self.weight += 1

    def __str__(self):
        # 避免打印出16进制内存地址  返回下面的数据
        return "my name %s 体重 %.2f" % (self.name, self.weight) # %.2f 浮点数打印两位


xm = Person('小鸟', 80)
xm.run()
xm.eat()
print(xm)