#!/usr/bin/python3

# 计数器
# while 条件:
#     满足条件的时候执行的代码

# 定义一个变量，也就是计数器

# 计数器一般都建议从0开始
i = 0
# 使用while进行判断


print("hello python\n"*5)

# 五次循环
while i<=5:
    print('hello python')
    i +=1
print("循环5次后i的值等于： {}".format(i))


# 循环计算

i = 0
sum = 0
while i <= 100:
    print("本次数：{}".format(i))
    sum = sum+i
    i +=1
print(sum)


p = 0
g = 0
yy = int(input("Please input:"))

while p <= yy:
    if p % 2 == 0:
        g = g+p
    p += 1

print(g)





