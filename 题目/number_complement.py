"""
找到一个数的反码
"""


def find_complement(num):
    """
    :param num: int
    :return: int
    """
    return int(bin(num).replace('0b', '').replace('1', 't').replace('0', '1').replace('t', '0'), 2)


if __name__ == "__main__":
    num = 10
    answer = find_complement(num)
    print(answer)