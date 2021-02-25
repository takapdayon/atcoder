def b192(s):

    ss = s[::2]
    sa = s[1::2]

    if len(s) == 1 and s.islower():
        return 'Yes'

    if ss.islower() and sa.isupper():
        return 'Yes'
    return 'No'

s = str(input())
print(b192(s))