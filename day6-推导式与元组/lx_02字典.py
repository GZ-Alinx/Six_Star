# 字典数无序数据类型
# 字典是key value k/y数据类型  key必须是唯一的  value可以重复可以为任意可支持的数据类型
# 使用双引号 或者单引号都行
#  key 就是字典的索引

d = {"name": '李雄', 'age': 25}
print(d['name'])
print(d['age'])
print(d)



# 字典的增删改查

# 增加、修改
d['name'] = '东汉末年'
print(d['name'])
# 如果key存在，则修改 如果不存在则 新建
d['sex'] = 'man'
print(d['sex'])

# 字典合并, 如果字典中有重复的键值 会直接覆盖

d1 = {'site': '深圳市'}
d.update(d1)
print(d)

# 字典查
d.get('web')  # 如果key 不存在不会报错
d['web']    # 如果不存在则会报错

d.keys()    # 获取字典中所有的key
d.values()  # 获取字典所有与的value

# 删除
del d['sex']  # 如果key 不存在则会报错
d.pop('age')  # 如果key 不存在则会报错
d.popitem()   # 删除字典中的最后的键值队，字典是无序的， 也就意味着还是随机删除
d.clear()     # 清空字典


