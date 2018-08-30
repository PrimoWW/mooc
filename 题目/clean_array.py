"""
remove duplicates from sorted array.

简单的来说就是给已经排序的序列做去重。
"""


def remove_duplicates(nums):
    """

    :param nums: list[int]
    :return: int
    """
    i = 0
    while True:
        if i <= len(nums)-1:
            if nums[i] == nums[i-1] and i > 0:
                nums.pop(i)
                i -= 1
            i += 1
            print(nums, i)
        else:
            break

    print(nums)
    return len(nums)


if __name__ == '__main__':
    nums = [1]
    length = remove_duplicates(nums)
    print(length)