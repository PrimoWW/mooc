"""
题目描述
    设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
    如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
    如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。
输入描述:
    有多组测试样例，每组测试样例包含两行，第一行为一个整数N（N<=100），
    第二行包含N个数(每个数不超过1000，空格分开)。
输出描述:
    每组数据输出一个表示最大的整数。
"""

# 思路， 判断两个数的权重关系的思想是AB > BA => A > B


def sort(n, list):
    m = int(n)
    for j in range(0, m):
        for i in range(0, m-1):
            if int(list[i]+list[i+1]) < int(list[i+1]+list[i]):
                list[i], list[i+1] = list[i+1], list[i]
    number = ''
    for num in list:
        number = number + num
    print(int(number))


n = input()
lst = input().split()
sort(n, lst)
