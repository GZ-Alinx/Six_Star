# 基础用法
print("基础用法")
def sum_2_num1():
    num1 = 10
    num2 = 20
    ret = num1 + num2
    return print(ret)


sum_2_num1()


# 函数使用传参使用 增加灵活性
print("传参用法")

# 形式参数
def sum_2_num2(num1, num2):
    ret = num1 + num2
    return print(ret)


# 实际参数传入
sum_2_num2(1,2)

