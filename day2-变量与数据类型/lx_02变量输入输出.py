# price_str = input("请输入单价: ")
# weight_str = input("请输入重量：")


#  计算金额
#  把重量和单价装换为数字类型

try:
    price = float(input("请输入单价: "))
    weight = float(input("请输入重量："))
    money = price * weight
    print('{:.2f}'.format(money))
except Exception as E:
    print("请输入正确的数字!  - [ {} ]".format(E))


# 格式化输出
#   %s  字符串
#   %d  整数
#   %f  浮点数

# 将a变成6位数  前面不够的用 0 补齐
a = 255
print("你的数字：%06d" %a)


