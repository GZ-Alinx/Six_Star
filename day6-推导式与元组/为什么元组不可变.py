# 元组数据可变为什么
# 列表数据可变为什么

# id 获取内存地址空间   内存地址空间 改变 数据就是从新开始  此时改变数据  等于新的数据

# 列表
a = [1, 2, 3, 4]
print(id(a),a)
a.append(2)
print(id(a),a)



print('-'* 20)
# 元组
b = (1, 2, 3, 4)
print(id(b), b)
b = b + (999,)
print(id(b), b)