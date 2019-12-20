# 多个参数收集
def args_max(*args):
    for i in args:
        print(i)


print(type(args_max(1, 'alinx', 342)))


def args_max1(**args):
    for i in args:
        print(i)

