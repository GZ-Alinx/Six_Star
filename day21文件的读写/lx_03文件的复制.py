# encoding=utf-8
# 小文件的复制
# f_read = open('1.txt', encoding='UTF-8')
# f_write = open('2.txt', 'w', encoding='UTF-8')
#
# text = f_read.read()
# f_write.write(text)
#
# f_read.close()
# f_write.close()
#
#
# # 大文件复制
# f_r = open('1.txt', encoding='UTF-8')
# f_w = open('3.txt', 'w')
#
# while True:
#     text = f_r.readline()  # 安装读取
#
#     # 如果没有读取到内容就break
#     if not text:
#         break
#
#     f_w.write(text)
#
# f_r.close()
# f_w.close()


# 切片取值 最佳操作  会自动关闭文件
with open('1.txt', 'r', encoding='UTF-8') as f:
    print(f.read()[0:2])


# with 是上下文管理器
"""
__enter__
__exit__   三个参数
"""