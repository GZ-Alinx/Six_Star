# 主要功能文件
card_list = []
def show_menu():
    """显示菜单"""

    print("""
    ********************************
    欢迎使用【名片管理系统】 V1.0
    1. 新建名片
    2. 显示全部
    3. 名片查询
    0. exit
    ********************************
    """)


def new_card():
    """新建名片"""
    print("-"*30)
    print("新建名片")
    name = input('name:')
    phone = input('phone:')
    email = input('mail:')
    qq = input('qq:')

    # 将用户信息保存到字典中
    card_dict = {
        'name': name,
        'phone': phone,
        'email': email,
        'qq': qq
    }
    card_list.append(card_dict)
    print(card_list)
    # 提示添加完成
    print("{} add Success~".format(card_list))


def show_all():
    """显示全部"""
    print("-"*30)
    print("显示全部")
    if len(card_list) == 0:
        print("not data")
        return
    for name in ['name', 'phone', 'qq', 'email']:
        print(name, end='\t\t')
    print("")
    for card_dict in card_list:
        print("{}{}{}{}".format(card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['email']))


def search_card():
    """查询名片"""
    pass