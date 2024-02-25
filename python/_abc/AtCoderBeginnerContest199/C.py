def t1(ans, is_t, leng, a, b):
    if is_t:
        x = ans[a]
        ans[a] = ans[b]
        ans[b] = x
    else:
        if a < leng:
            aa = a + leng
        else:
            aa = a - leng
        if b < leng:
            bb = b + leng
        else:
            bb = b - leng
        x = ans[aa]
        ans[aa] = ans[bb]
        ans[bb] = x
    return ans

def c199(n, s, q, tabl):

    leng = int(len(s)//2)
    ans = s
    is_t = True
    for i in range(q):
        if tabl[i][0] == 2:
            is_t = not is_t
        else:
            ans = t1(ans, is_t, leng, (tabl[i][1] - 1), (tabl[i][2] - 1))

    if is_t:
        return ''.join(ans)
    return ''.join(ans[leng:] + ans[:leng])

    return ans

n = int(input())
s = list(str(input()))
q = int(input())
tabl = [list(map(int, input().split())) for i in range(q)]
print(c199(n, s, q, tabl))
