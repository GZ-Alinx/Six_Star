# 函数返回值 是函数处理完后返回给调用者的数据


def sum_sum(num1, num2):
    d = num1 * num2
    return num1 + num2, d
    # return 表示函数结束执行 下面的代码不会再执行

ret = sum_sum(10,20)
print(ret)

