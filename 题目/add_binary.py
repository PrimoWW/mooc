"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100"
"""


def add_binary(a, b):
    """
    :param a: str
    :param b: str
    :return: str
    """
    return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    a = '11'
    b = '1'
    answer = add_binary(a, b)
    print(answer)
