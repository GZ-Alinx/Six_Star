a = int(input(':'))
b = int(input(':'))
if a == 1:
    print('ok')
else:
    print('error')

if a >= 60 and a <= 100:
    print('你很优秀：good')

if a >= 60 or b >= 60:
    print('成绩ok')

is_smpile = False

if not is_smpile:
    print("正确")
else:
    print("错误")

# 嵌套判断语句

if 60 <= a <= 70 and type(a) == int:
    print("及格了")
elif 70 <= a <= 80:
    print("非常的不错")
elif 80 <= a < 90:
    print("你很优秀啊")
elif 90 <= a <= 100:
    print("学霸")
elif a >= 100:
    print("你是NO.1")
else:
    print("需要努力哦")
