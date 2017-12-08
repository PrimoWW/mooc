"""
创建并测试一个函数，然后读取__doc__属性，在检查他的类型
"""
def factorial(n):
    """this function is used to find n**(n-1)**(n-2)**...**1"""
    return 1 if n==1 else n * factorial(n-1)

if __name__=="__main__":
    print(factorial(30))
    print(factorial.__doc__)
    print(type(factorial))