# 匿名函数 lambda
# 不按常规方式创建函数  正常是需要def创建函数的， 而匿名函数 lambda 即可创建


# lambda 参数列表: 变量(表达式)
# 返回的是函数的对象 所以要用变量接收
ret = lambda x, y: x + y
print(ret(2, 3))


infors = [{'name':'123', 'age': 20}, {'name': '456','age': 22}, {'name': '444', 'age': 25}]
# 针对列表种的字典排序
infors.sort(key=lambda x: x['age'])
# 对比的值要同种类型 否则不支持
print(infors)


def test(a, b, func):
    ret = func(a, b)
    return ret


num = test(4, 5, lambda x, y: x + y)