import bisect

N = int(input())
alist = list(map(int, input().split()))

alist.sort()
max_length = len(alist)
ans = 0
for i in alist:
    ans += max_length - bisect.bisect_right(alist, i)

print(ans)