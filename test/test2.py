n = int(input()) # 组数

def find_ss(all_str):
    for str_lis in all_str:
        flag = 0
        length = len(str_lis)
        for i in range(length):
            target = str_lis.pop(0)
            str_len = len(target)
            for j in range(str_len):
                if target in str_lis or target[::-1] in str_lis:
                    flag += 1
                    break
                target = target[1:] + target[0]
        if flag > 0:
            print('Yeah')
        else:
            print('Sad')

all_str = []

for i in range(n):
    num_str = int(input())
    str_lis = []
    for j in range(num_str):
        str_lis.append(str(input()))
    all_str.append(str_lis)
find_ss(all_str)
