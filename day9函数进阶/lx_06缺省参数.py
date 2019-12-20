# 缺省参数

g_list = [3, 1, 4]
g_list.sort(reverse=True)
print(g_list)


def print_info(name, sex=True, title=''):
    """
    :param name: 姓名
    :param sex: 性别  True 男  False 女
    :param title: 职位
    """
    sex_text = '男生'
    if not sex:
        sex_text = '女生'
    print("%s%s is %s" % (title, name, sex_text))


print_info('小明', False)