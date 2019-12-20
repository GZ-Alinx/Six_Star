# 集合创建

s = {1, 2, 3, 4}
print(type(s))
# 创建空集合

l = [1, 2, 3]
print(set(l))

# 集合推导式
a = {x for x in 'asdfasdfasdf'}
print(a)

# 集合方法
s.add(4)
print(s)
s.update([11, 22, 13, 14])
print(s)
s.remove(14)
print(s)
s.discard(5)  # 如果数据不存在，也不会报错
s.clear()  # 清空集合 清空后就是一个 a()

# 集合遍历
for i in s:
    print(i)





print("列表去重" * 10)
# 列表去重  两种方法


t = [1, 2, 34, 4, 5, 6, 7, 8, 9]
g = [1, 2, 3, 53, 4, 2, 3, 4, 5, 767, 8, 9, 0, ]
print(type(t), type(g))
dd = set(t + g)
print(dd)


print('-'*20)
e = []
for i in g:
    if i not in e:
        e.append(i)
print(e)