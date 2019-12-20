# 不同的子类去调用相同的夫类方法 得到不同的结果 就是多态


# 多态案例
# 多个类多用一个父类 成为多态

class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s" % self.name)


class xtq(Dog):
    def game(self):
        print("%s 66666" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, doog):  # 参数？还是
        print("%s in %s sssss"% (self.name, doog.name))
        doog.game()


# 创建对象
wc = Dog('李雄')
xm = Person('董小姐')
xm.play_with_dog(wc)
xt = xtq('ddd')
xt.game()