# 案例
"""
游戏类：
历史最高分： 类属性
玩家姓名： 实例属性

游戏帮助信息： 静态方法
显示历史最高分： 类方法
开始游戏： 实例方法
"""


class Game(object):
    top_score = 0

    def __init__(self, name):
        self.name = name

    # 在方法中如果需要访问实例属性又要访问类属性，那么我们把它定义成它实例方法
    # 类只有一个，在实例方法中，可以使用类名.的方式调用类属性
    def start_game(self):
        print("[%s]开始游戏..." % self.name)
        Game.top_score = 900
    @classmethod  # 类方法
    def show_top(cls):  # 由哪一个类创建出来的就指向哪一个类
        print("游戏的最高分是：", cls.top_score)

    @staticmethod # 静态方法
    def show_help():  # 既不调用类方法，也不调用实例方法
        print("帮助信息： 方向键进行移动。。。")


# 查看帮助信息
Game.show_help()
# 查看游戏最高分
Game.show_top()
# 创建对象开始游戏
game = Game('李雄')
game.start_game()
# 游戏结束，显示最高分
Game.show_top()