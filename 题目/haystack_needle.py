"""
bisect是一个排序模块，操作前确保列表是排了序的（可以用sort（）方法）

里面主要有两类方法：bisect 和 insort：

    1.bisect(list， number)，返回将number插入list后number在list
      中的位置，但是不会改变list。即只是告诉你，number插入的位置，
      默认是右插入，还有两个方法bisect_left和bisect_right
    2.insort(list, number), 将改变list的值，即把number插入list，
      其他方面感觉和bisect没什么区别，就是一个告诉你位置，一个返回
      插入后的列表。

感觉很少见啊这个模块，也许哪天用上了也说不定。

by Primo
"""
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # 用特定的bisect函数来计算元素应该出现的位置
        offset = position * '  |'  # 利用该位置来确定需要几个分隔符
        print(ROW_FMT.format(needle, position, offset))  # 吧元素和其应该出现的位置打印出来


if __name__ == "__main__":
    if sys.argv[-1] == 'left':  # 根据命令上的最后一个参数来选择bisect函数
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print(dir(bisect))  # 看看模块里面有什么

    print('DEMO:', bisect_fn.__name__)  # 把选定的函数在抬头打印出来
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
