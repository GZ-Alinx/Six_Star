# 递归求和
def sum_numbers(num):
    if num == 1:
        return 1
    return num + sum_numbers(num -1)


print(sum_numbers(3))