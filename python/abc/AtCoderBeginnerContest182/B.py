def b182(n, alist):

    ans = [0, 0]

    for i in range(2, max(alist)+1):
        count = 0
        for w in alist:
            if w % i == 0:
                count += 1
        if ans[0] <= count:
            ans[0] = count
            ans[1] = i

    return ans

n = int(input())
alist = list(map(int, input().split()))
print(b182(n, alist)[1])