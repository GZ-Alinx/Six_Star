#  父类覆盖方法
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

    def bark(self): # 重写了父类方法  覆盖了父类方法
        print("很好听的叫")


xt = xtq()
xt.eat()
xt.bark()
xt.drintk()
xt.fly()
