# 递归函数示例
def sum_numbers(num):
    print(num)

    if num == 1:
        return
    sum_numbers(num - 1)


sum_numbers(3)