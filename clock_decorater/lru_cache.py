"""
functools.lru_cache实现了备忘功能，他把耗时的函数的结果保存起来，
避免传入相同的参数是重复计算

"""
from clock_decorater.clockdeco import clock
import functools


@clock
def fibonacci_1(n):
    if n < 2:
        return n
    return fibonacci_1(n-2) + fibonacci_1(n-1)


@functools.lru_cache()
@clock
def fibonacci_2(n):
    if n < 2:
        return n
    return fibonacci_2(n-2) + fibonacci_2(n-1)


if __name__ == "__main__":
    print(fibonacci_1(6))
    print(fibonacci_2(6))