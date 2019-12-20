"""
单继承 多继承
子类拥有父类中的特性，使用父类代码再子类中可以重复使用
"""


class Animal:
    def eat(self):
        print('吃')

    def drintk(self):
        print("喝")


class Dog:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")


# 以上重复的方法 不同的类 可否重用？
wc = Dog()
wc.eat()


# 使用继承开发
class Animal:  # 相当于父类
    def eat(self):
        print('吃')

    def drintk(self):  # 相当于子类
        print("喝")


class Dog(Animal):

    def bark(self):
        print("叫")


# 子类拥有父类的所有方法
wcc = Dog()
wcc.eat()
wcc.bark()
