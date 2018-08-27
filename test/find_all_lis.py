#求和等于target的所有组合
import copy
end, target = 5, 5
def good(start, end, target, li):

    if target == 0:
        li.sort()
        print(' '.join(li))
        return
    if target < 0 or start > end:
        return


    li1 = copy.deepcopy(li)
    li2 = copy.deepcopy(li)

    li1.append(str(start))

    good(start+1, end, target-start, li1)
    good(start+1, end, target, li2)
li = []
good(1, end, target, li)