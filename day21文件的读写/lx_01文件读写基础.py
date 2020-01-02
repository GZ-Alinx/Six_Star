# -*- coding: utf8 -*-
"""
# open函数， 打开文件并且返回一个操作对象
    read 读取内容
    write 写入内容
    close 关闭文件
"""

# 打开文件要关闭 否则会消耗内存空间
# 读取一次后就会把指针移动到后面

f = open('1.txt')
print(f.read())
f.close()

ff = open('1.txt', 'w')
ff.write('123\n')
