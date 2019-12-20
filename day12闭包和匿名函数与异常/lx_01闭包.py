#  闭包函数
"""
闭包三要素：
    1. 函数的嵌套
    2. 内层函数是用到了外层函数的局部变量
    3. 外层函数返回内层函数的引用
"""


def test(a):
    # 在函数内部再次定义了函数，并且这个函数使用到了外部汉书的局部变量
    # 那么就将这个函数以及用到一些变量称之为闭包

    def tets_in(b):
        print('zai test in def zhong a:"', b)
        return a + b

    # 这里返回了闭包的结果
    return tets_in


ret = test(10)  # 这里的10给的是参数a
print(ret(30))  # 这里的30给的是参数b

# 可以简写
ret = test(10)(30)
