"""
Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.
U(up)D(down)R(right)L(left)
eg:
input: "UDRL"
output: True
思路 判断能不能回到原点 也就是转化成 R和L，U和D的数量是不是相等。简单啦
"""


def judge_circle(moves):
    """
    :param moves: str
    :return: bool
    """
    if moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D'):
        return True
    else:
        return False


if __name__ == '__main__':
    moves = 'RRLLUUDD'
    print(judge_circle(moves))
