# 继承的传递性
class Animal:  # 相当于父类
    def eat(self):
        print('吃')

    def drintk(self):  # 相当于子类
        print("喝")


class Dog(Animal):

    def bark(self):
        print("叫")


class xtq(Dog):
    def fly(self):
        print("飞")


xt = xtq()
xt.eat()
xt.bark()
xt.drintk()
xt.fly()
