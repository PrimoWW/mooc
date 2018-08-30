"""
用户定义可调用类型
"""
import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)  # 将_items序列随机排序

    def pick(self):
        try:
            return self._items.pop()  # 拿出最后一个元素
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        """
        __call__方法让对象变得看起来更像函数，
        如下面例子所示：
        bingo.pick()和bingo()
        有相同的效果
        """
        return self.pick()


if __name__ == "__main__":
    bingo = BingoCage(range(10))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))

