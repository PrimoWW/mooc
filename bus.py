"""
通过这个例子解释下浅复制和深复制
"""


import copy


class Bus:
    def __init__(self, passengers=None):
        if passengers == None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == "__main__":
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)

    print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))

    bus1.drop('Bill')

    print('bus2', bus2.passengers)
    print('bus3', bus3.passengers)

    a = [1, 2]
    b = [a, 3]
    a.append(b)
    print(a)