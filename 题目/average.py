"""
闭包的例子，还是迷迷糊糊的
"""
def make_averager_1():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


def make_averager_2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count
    return averager


if __name__ == "__main__":
    avg = make_averager_2()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    print(avg.__code__.co_filename)
    print(avg.__code__.co_freevars)
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_flags)