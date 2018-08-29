#根据x + y = x|y，给定x, 求满足要求的第 k 个 y
#例如 x = 4 , k = 2 时， y = 2
# x =0b100 y=0b10

def find_y(x, k):
    """
    :param x: int
    :param k: int
    :return: int
    """
    y = 1
    l_out = []
    while len(l_out) < k:
        if x + y == x | y:
            l_out.append(y)
        y += 1
    print(l_out[-1])


if __name__ == "__main__":
    find_y(10, 2)