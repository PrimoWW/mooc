"""
给出二叉树前序和中序遍历的字符串推出后序遍历的字符串
例如：
>>ABC
>>BAC

>>CBA
"""


def get_post(pre_order, in_order):
    if pre_order == []:
        return ''
    else:
        # 中序的根节点的索引
        in_root = in_order.index(pre_order[0])

        root = pre_order[0]

        pre_left_child = pre_order[1:1+in_root]
        pre_right_child = pre_order[1+in_root:]

        in_left_child = in_order[0:in_root]
        in_right_child = in_order[1+in_root:]

        post_left_child = get_post(pre_left_child, in_left_child)
        post_right_child = get_post(pre_right_child, in_right_child)

        return str(post_left_child) + str(post_right_child) + pre_order[0]


while True:
    pre_order = input()
    in_order = input()
    pre_order = list(pre_order)
    in_order = list(in_order)
    lis = get_post(pre_order, in_order)
    print(lis)
