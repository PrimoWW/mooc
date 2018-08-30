"""
原题目太长了，简化一下：
一个数如果能被本身每一位整除，则为自分数(self dividing number)
eg: 128 % 1 = 0, 128 % 2 ==0, 128 % 8 ==0

要求：
返回left和right区间内所有的自分数
"""


def self_dividing_numbers(left, right):
    """
    :param left: int
    :param right: int
    :return: List[int]
    """
    answer = []
    for all_number in range(left, right+1):
        number_of_true = 0
        for str_bit in list(str(all_number)):
            int_bit = int(str_bit)
            if int_bit != 0:
                if all_number % int_bit == 0:
                    number_of_true += 1
        if len(list(str(all_number))) == number_of_true:
            answer.append(all_number)
    return answer


if __name__ == '__main__':
    left = 1
    right = 10000
    answer = self_dividing_numbers(left, right)
    print(answer)