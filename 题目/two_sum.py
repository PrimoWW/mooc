"""
Given an array of integers,
return indices of the two numbers such that they add up to a specific target.
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

本题来源于LeetCode,因为leetcode上运行测试用例，所以实现上有区别
"""


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length = len(nums)
    answer = []
    for first in range(length):
        for second in range(length):
            print(nums[first], nums[second])
            if nums[first] + nums[second] == target and first != second:
                answer.append(first)
                answer.append(second)
                return answer


if __name__ == "__main__":
    nums = [0, 4, 3, 0]

    target = 0
    answer = two_sum(nums, target)
    print(answer)

