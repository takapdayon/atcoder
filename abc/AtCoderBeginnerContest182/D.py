def d182(n, alist):

    ans = 0
    maxti = 0
    now = 0
    imamade = 0

    if len(alist) == 1:
        return alist[0] if alist[0] > 0 else 0

    for i in alist:
        ans = max(ans, (maxti + now))
        imamade += i
        now += imamade
        maxti = max(maxti, imamade)

    ans = max(ans, imamade)

    return ans

n = int(input())
alist = list(map(int, input().split()))
print(d182(n, alist))