#  主程序入口文件
import card_tools

while True:
    # TODO(alinx) 显示系统菜单
    card_tools.show_menu()
    action = input("please your action: ")
    print("you action:{}".format(action))
    if action in ['1', '2', '3']:
        if action == '1':
            card_tools.new_card()
        elif action == "2":
            card_tools.show_all()
        elif action == "3":
            card_tools.search_card()
        else:
            print("输入正确的参数")
    elif action in ['0']:
        print("welcome try use card system")
        break
    else:
        print('try input')