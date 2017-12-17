l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
l3 = l1

l1.append(4)
l1[1].append(33)
l1[2] += (10, 11)

print(l1)
print(l2)
print(l3)