"""
try:
    需要执行的代码
except:
    出现异常后进行怎么样的处理
"""


try:
    num = int(input(':'))
    print(num)
except:
    print('error')

print('.')


# 捕获异常的时候会有很多类型的错误  我们可以精确的去捕获从而得到具体的问题 然后具体处理
# 捕获不同的错误类型

try:
    pass
except Exception as E:  # Exception 就是一个就具体的错误类型
    # 程序抛出的异常前的错误 就是错误类型  直接就可以拿到错误类型做判断了
    print(E)
else:
    print('7787')
