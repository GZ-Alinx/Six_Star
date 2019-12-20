# 函数嵌套调用


def Daemon1():
    print('*'*20)


def Daemon2():
    print(">"*10)


Daemon1()
Daemon2()

###

def print_line(char, times):
    print(char * times)


def print_lines(char, times, u):
    for i in range(u):
        print_line(char, times)


print_lines("*", 20, 7)
