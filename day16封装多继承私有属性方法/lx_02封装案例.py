"""
需求

1.房子有户型、总面积、家居名称列表
2.家居有名字和占地面积 4 2 2.5
3.将上面的三家家居添加到房子中
4.打印房子的时候，要求输出户型，总面积，剩余面积，家居名称列表

分析
    类名: 房子类(House) 家居类(HouseItem)
    属性: 房子，户型，总面积，剩余面积，家居列表
        家居： 名字(name), 占地面积(area)

方法：  
        房子： __init__, __str__,add_item
        家居： __init__, __str__
"""


class HouseItem:
    """家居类"""

    def __init__(self, name, area):
        """
        :param name: 家居名称
        :param area: 占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地面积是 %.2f平米" % (self.name, self.area)


bed = HouseItem("大床", 4)
chest = HouseItem('柜子', 3)
table = HouseItem("桌子", 2.5)
print(bed, "\n", chest, "\n", table, "\n")


class House:

    def __init__(self, house_type, area):
        """
        :param house_type: 户型
        :param area: 总面积
        """
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 默认没有家居
        self.item_list = []

    def __str__(self):
        # 打印对象时生效  而非类本身
        return ("户型：%s总面积: %.2f剩余面积：%.2f家居%s" %
                (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加：%s" % item)
        if item.area > self.free_area:
            print("家居面积太大了")
        self.item_list.append(item.name)
        self.item_list = []
        print(item.name, item.area)


my_home = House("很大的房子", 120)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)















