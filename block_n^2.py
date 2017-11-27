"""
题目：
在一个九宫格内，从（1,1）走到（3,3）有多少种走法（只考虑步数最骚的情况）
并推广至n*n的方格

主要思路：
我的理解是从终点回溯，走到（n，n）只有两种情况：（n-1，n）和（n，n-1）
走到边上时（row=1 or col=1）就没有其他选择了，径直回到起点

注：
由于采用的是递归策略，所以时间复杂度爆炸，粗略算了一下应该是C（2^n）左右
当然，也可以用数学公式进行推导，那就快得很了

"""
import time

ROW = 3
COL = 3


def digui(row, col):
    if row == 1 or col == 1:
        return 1
    else:
        return digui(row-1, col) + digui(row, col-1)


def main(row, col):
    start = time.time()
    print("走法的数量为："+str(digui(row, col)))
    end = time.time()
    print(start)
    print(end)
    print("所用时间： "+str(end-start))


if __name__ == "__main__":
    main(ROW, COL)
