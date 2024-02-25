
def sort_num(n, desc=0):

    a = list(map(int, list(str(n))))
    x = 0

    if desc:
        a.sort()
    else:
        a.sort(reverse=True)

    a = list(map(str, a))

    return int(''.join(a))

def c192(n, k):

    ans = n
    for i in range(k):
        ans = sort_num(ans) - sort_num(ans, 1)
    return ans

n, k = map(int, input().split())
print(c192(n, k))
