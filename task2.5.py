import os


def fun():
    with open('dataset_24465_4.txt') as r, open('re.txt', 'w') as w:
        lines = r.readlines()
        lines.reverse()
        for line in lines:
            w.write(line)


def fun2():
    with open('res.txt', 'w') as r:
        r.writelines("\n".join(
            sorted(set([path for path, dirs, files in os.walk('main') for file in files if file.endswith('.py')]))))


from functools import partial


def mod_checker(x, mod=0):
    return lambda y: y % x == mod


mod3 = mod_checker(3)
print(mod3(3))
print(mod3(4))

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4))
