# for 循环遍历

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in l:
    print(num)

# range 函数
for i in range(10):  # 10括号里面10是边界
    print(i)
# range(1, 11) 从1开始到11前一位结束  等于1 - 10

# 99 乘法表
for i in range(1, 10):   # 外层循环控制行数
    for j in range(1, i+1):  # 内层循环控制列数
        print("%d x %d = %d"%(j, i, i*j), end='\t')
    print("")