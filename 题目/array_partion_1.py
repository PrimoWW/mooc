"""
given an array of 2n integers,
your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn)
which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4)

思路：数组分区问题。应该先按顺序进行排序，再统计0, 2, 4...索引的和
"""


def array_partion_1(nums):
    """
    :param nums: List[int]
    :return: int
    """
    return sum(sorted(nums)[::2])


if __name__ == "__main__":
    nums = [2, 3, 1, 6, 36, 34]
    answer = array_partion_1(nums)
    print(answer)