# new 方法


class MusicPlayer(object):

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        # 为对象分配空间
        # 返回对象的引用
        return super().__new__(cls) # 如果不重写new方法，那就会覆盖父类的new方法
        # 那如果想要重新定制那就必须要重写
        # 默认每一次都会重新重新分配一个内存地址
        #


playyerq = MusicPlayer()
playyer2 = MusicPlayer()
print(playyerq)
print(playyer2)
