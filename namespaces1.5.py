parents = {"global": []}
names = {"global": []}

n = int(input())


def find_var_in_names(namesp, arg):
    if arg in names[namesp]:
        return namesp
    else:
        for key, vals in parents.items():
            if namesp in vals:
                return find_var_in_names(key, arg)


def read_data():
    global n
    if n == 0:
        return
    else:
        n -= 1
        cmd, namesp, arg = input().split()
        if cmd == "add":
            if namesp in names.keys():
                names[namesp].append(arg)
        elif cmd == "create":
            parents[arg].append(namesp)
            names[namesp] = []
            parents[namesp] = []
        else:
            print(find_var_in_names(namesp, arg))
        read_data()


read_data()
