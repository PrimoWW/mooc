"""
Given a non-negative integer num,
repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38,
the process is like: 3 + 8 = 11,
1 + 1 = 2. Since 2 has only one digit, return it.
"""


def add_digits(num):
    """
    :param num: int
    :return: int
    """
    next_num = num
    while True:
        print(next_num)
        list_num = list(str(next_num))
        next_num = 0
        for i in list_num:
            next_num += int(i)
        if next_num < 10:
            break
    return next_num



if __name__ == '__main__':
    num = 38
    print(add_digits(num))
