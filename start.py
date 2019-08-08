fib = lambda x: 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31))


def input_sums():
    n = int(input())
    sum = 0
    for i in range(n):
        sum += int(input())
    print(sum)


# print(type(input_sums))
# print(id(input_sums))
#
# x = 3
# y = x
# print(id(3))
# l = [1, 2]
# print(type(id(l)))
# print(id([1, 2]))
# print([1, 2] is [1, 2])
# y += 1
# print(x)
# print(y)
#
# objects = [1, 4, 3, 4]
# uniq = []
# for item in objects:
#     if not (item in uniq):
#         uniq.append(item)
# print(len(uniq))


def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return closest_mod_5(x + 1)


# print(closest_mod_5(6))


def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res


# print(s(11, 10, 10))

def combinations(n, k):
    return 1 if k == 0 else 0 if k > n else combinations(n - 1, k) + combinations(n - 1, k - 1)


n, k = map(int, input().split())
print(combinations(n, k))


