class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        return self.capacity >= self.count + v

    def add(self, v):
        self.count += v


class Buffer:
    def __init__(self):
        self.data = []

    def add(self, *a):
        self.data += a
        self.print_extra_numbers()

    def get_current_part(self):
        return self.data

    def print_extra_numbers(self):
        if len(self.data) >= 5:
            print(sum(self.data[0:5]))
            del (self.data[0:5])
            self.print_extra_numbers()


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part())
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part())
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part())


class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar()
a.foo()

c = A()

print(a.val)
print(b.val)
print(c.val)
