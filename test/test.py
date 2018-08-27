n, t = list(map(int, input().split()))
one_lis = list(map(int, input().split()))
res = 0
sample = one_lis * t

xuliehua = []
for i in range(len(one_lis)):

    fps = 0

    for j in range(i+1, len(one_lis)):
        if sample[j] >= sample[i]:
            fps += 1
    xuliehua.append(fps)



print(xuliehua)