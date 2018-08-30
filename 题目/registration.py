"""
这个例子展示出了装饰器的一个特性，
它们在被装饰的函数定义后立即运行（这通常是在导入时（即Python加载模块时））

而被装饰函数只在明确调用时运行
"""

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


def f2():
    print('running f2()')


f2 = register(f2)


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()
