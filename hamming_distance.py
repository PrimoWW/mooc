"""
return hamming distance
eg:
input(1, 4)
return 2
because 1(0001) 4(1000) they have two different bits.
思路很简单，python提供轮子了。xy做异或找到不相同的位，再统计1出现的个数
"""


def hamming_distance(x, y):
    """
    :param x: int
    :param y: int
    :return: int
    """
    return bin(x ^ y).count('1')


if __name__ == "__main__":
    x = 2 ** 30
    y = 123
    print(hamming_distance(x, y))
