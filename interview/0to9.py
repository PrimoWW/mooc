import copy
# a = [0,1,2,3,4,5,6,7,8,9] # 数字数组
# b = [0,1,1,1,0,1,1,1,1,0] # 对应的布尔值数组
# b = list(map(int,input().strip().split()))
b = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
index = []
for i in range(0,len(b)):
    if b[i] == 1:
        b[i] = str(i) # 将布尔值为1的位置赋予对应的数值
    if b[i] == 0:
        index.append(i) # 记录布尔值为0的位置索引
        b[i] = '' # 同时赋予空
res = [b]

for ind in index:
    for i in range(len(res)):
        c = copy.copy(res[i])
        c[ind] = str(ind) # 对结果列表中的每个组合依次添加布尔值为0的位置所对应的数字
        res.append(c)

for i in range(len(res)):
    res[i] = ''.join(res[i])
res.sort() # 排序
for i in res:
    print(i)