def b204(n, alist):

    ans = 0

    for i in alist:
        if i > 10:
            ans += i - 10

    return ans

n = int(input())
alist = list(map(int, input().split()))
print(b204(n, alist))
