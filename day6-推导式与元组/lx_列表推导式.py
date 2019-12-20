

# 列表推导式
res = [(x, y) for x in range(10) for y in range(10) ]
print(res)
# 相当于下面的代码 把数据类型直接变更位列表
# for i in range(10):
#     for y in range(10):
#         print(i,y)

reset = [(x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8]
print(reset)

print('-'*100)

resett = [(o,p) for o in range(100) if o % 2 == 0 for p in range(101,1000) if p % 7 == 0 ]
print(sorted(resett))