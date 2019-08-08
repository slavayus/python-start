# try:
#     # foo()
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ArithmeticError:
#     print('ArithmeticError')
# except AssertionError:
#     print('AssertionError')


def third():
    classes = {}
    for _ in range(int(input())):
        line = input().split(':')
        classes[line[0].strip()] = ['object'] if len(line) == 1 else line[1].strip().split(' ')

    search_list = []

    def search_super_clas(curr_except_class):
        if len(search_list) == 0:
            return False
        curr_clas = search_list.pop()
        if curr_except_class == curr_clas:
            return True
        elif curr_clas in classes and classes[curr_clas].__contains__(curr_except_class):
            return True
        elif curr_clas in classes:
            search_list.extend(classes[curr_clas])
            return search_super_clas(curr_except_class)
        else:
            return search_super_clas(curr_except_class)

    except_stack = []
    for _ in range(int(input())):
        clas = input()
        res = False
        for curr_except in except_stack:
            search_list = [clas]
            res = res or search_super_clas(curr_except)
        except_stack.append(clas)
        if res:
            print(clas)


class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, val):
        if val > 0:
            super().append(val)
        else:
            raise NonPositiveError()


import timeit

timeit.Timer('s.append("something")', 's = []').timeit()
timeit.Timer('s += ["something"]', 's = []').timeit()
