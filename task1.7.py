class Base:
    def __init__(self):
        self.val = 0

    def add_one(self):
        self.val += 1

    def add_many(self, x):
        for i in range(x):
            self.add_one()


class Derived(Base):
    def add_one(self):
        self.val += 10


a = Derived()
a.add_one()

b = Derived()
b.add_many(3)


# print(a.val)
# print(b.val)


class A:
    def foo(self):
        print("A")


class B(A):
    pass


class C(A):
    def foo(self):
        print("C")


class D:
    def foo(self):
        print("D")


class E(B, C, D):
    pass


# print(E.mro())
# E().foo()


# classes = {}
# for _ in range(int(input())):
#     line = input().split(':')
#     classes[line[0].strip()] = ['object'] if len(line) == 1 else line[1].strip().split(' ')
#
# search_list = []
#
#
# def search_super_clas(s_clas):
#     if len(search_list) == 0:
#         return 'No'
#     c_clas = search_list.pop()
#     if s_clas == c_clas:
#         return 'Yes'
#     elif c_clas in classes and classes[c_clas].__contains__(s_clas):
#         return 'Yes'
#     elif c_clas in classes:
#         search_list.extend(classes[c_clas])
#         return search_super_clas(s_clas)
#     else:
#         return search_super_clas(s_clas)
#
#
# for _ in range(int(input())):
#     sup_clas, clas = input().split()
#     search_list = [clas]
#     print(search_super_clas(sup_clas))


class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())


def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0


test()

import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, o):
        super().append(o)
        self.log(o)


a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)

LoggableList([1, 2, 3]).append(4)
