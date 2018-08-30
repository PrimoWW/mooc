"""
题目：在一个数列里找出所有的peak*
       *peak：if a[i] > a[i-1] and a[i] > a[i+1], then a[i] is a peak.

思路：if a[i] is a peak, a[i+1] must not be a peak.
     then we can jump over the a[i+1], and directly judge a[i+2]
"""

def peak(lis):
    length = len(lis)
    i = 0
    answer = []
    while True:
        if i == 0:
            if lis[i] > lis[i+1]:
                answer.append(lis[i])
                i = i + 2
            else:
                i = i + 1
        if i == length - 1:
            if lis[i] > lis[i-1]:
                answer.append(lis[i])
                break
            else:
                break
        if i == length - 2:
            if lis[i-1] < lis[i] > lis[i+1]:
                answer.append(lis[i])
                i = i + 1
            else:
                i = i + 1
        if 0 < i < length-2:
            if lis[i-1] < lis[i] > lis[i+1]:
                answer.append(lis[i])
                i = i + 2
            else:
                i = i + 1

        print(i)

    return answer

def main(lis):
    answer = peak(lis)
    print(answer)

if __name__ == "__main__":
    lis = [1,2,4,2,6,4,6,3,6,7,9,4,4,4,4,3,2,4,6,8,9,0,4,2,5,6,7,8,5,8,6,8,5,9]
    main(lis)