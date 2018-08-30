"""
如果一个对象是可散列的（hash），那么在他的生命周期，它的散列值是不变的
原子不可变数据类型都是可散列的（str，bytes和数字类型），元组的话，必须其中包含的所有元素都是
可散列类型的情况下，他才是可散列的
"""

tt = (1, 2, (30, 40))

tf = (1, 2, frozenset([30, 40]))

tl = (1, 2, [30, 40])


print(hash(tt))
print(hash(tf))

try:
    print(hash(tl))

except TypeError:
    print("TypeError")