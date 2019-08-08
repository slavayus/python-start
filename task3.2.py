def fun():
    s = input()
    a = input()
    b = input()
    replaces = 0
    while s.__contains__(a) and replaces <= 1000:
        s = s.replace(a, b)
        replaces += 1

    print('Impossible' if replaces > 1000 else replaces)


line, sub = (input() for _ in range(2))
subs = 0
while len(line) >= len(sub):
    subs += 1 if sub == line[:len(sub)] else 0
    line = line[1:]

print(subs)
