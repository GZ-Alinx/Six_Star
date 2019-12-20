def input_password():
    """user input password"""
    pwd = input('pass:')
    if 6 <= len(pwd) >= 18:
        return pwd
    ex = Exception('密码长度不够')
    raise ex  # 抛出异常 和return不一样的是 raise是把异常抛出  而不是返回数据
    # 当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。
    # 一旦执行了raise语句，raise后面的语句将不能执行。


try:
    user_pwd = input_password()
    print(user_pwd)
except Exception as e:
    print('发现错误：', e)