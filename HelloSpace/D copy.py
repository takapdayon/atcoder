def dd(s):
    t = []
    rev = True
    for i in s:
        if i != "R":
            if rev:
                if t and t[-1] == i:
                    t.pop()
                else:
                    t.append(i)
            else:
                if t and t[0] == i:
                    t.pop(0)
                else:
                    t.insert(0, i)
        else:
            rev = not rev
    if not rev:
        t.reverse()
    return ''.join(t) if t != [] else ''

s = list(str(input()))
print(dd(s))