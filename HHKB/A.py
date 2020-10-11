def keyboard(s, t):

    return t.upper() if s == "Y" else t


s = str(input())
t = str(input())
print(keyboard(s, t))
