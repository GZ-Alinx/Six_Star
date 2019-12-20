# 1.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
import time

Down_Ball = 100
After_Height = 0
Height = 0


for i in range(1,11):
    # 回弹的高度
    UP_Height = Down_Ball / 2
    # 每次落下的高度
    Down_Ball1 = UP_Height + UP_Height
    # 一共落下的高度
    After_Height += Down_Ball1
    Down_Ball = Down_Ball / 2
    print("第%s次的反弹距离是：%s米 一共经过%s米"% (i, UP_Height, After_Height))
    time.sleep(1)




# 2.一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

import time

Factor_Number = 1000
for i in range(1, 1001):
    if i % Factor_Number and i <= Factor_Number:
        print(i)
        time.sleep(1)



# 3.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# 设str为字符串
# str.isalnum() 所有字符都是数字或字母
# str.isalpha() 所有字符都是字母
# str.isdigit() 所有字符都是数字
# str.islower() 所有字符都是小写
# str.isupper() 所有字符都是大写
# str.istitle() 所有单词都是首字母大写，像标题
# str.isspace() 所有字符都是空白字符或\t或\n或\r


your_str = input("请输入您的字符：")

str_sum1 = 0
str_sum2 = 0
str_sum3 = 0
str_sum4 = 0

for i in your_str:
    if i.isdigit():
        print("数字字符：%s"% i)
    elif i == " ":
        print("空格字符： %s"%i)
    elif i.islower():
        print("小写字母：%s"%i)
    elif i.isupper():
        print("大写字符： %s"% i)
    else:
        print('特殊字符：%s'%i)


i = 1000
n = 0
max = 0
while i >= n:
    n+=1
    max = n+n+1
    if max <= 1000:
        print("包括：", max)
    else:
        break







