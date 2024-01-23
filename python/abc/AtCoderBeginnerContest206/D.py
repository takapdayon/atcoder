N = int(input())
alist = list(map(int, input().split()))

max_length = len(alist) - 1
ans = set()
for i in range(max_length):
    if alist[i] == alist[max_length - i]:
        continue
    ans |= set([alist[i], alist[max_length - i]])

print(len(ans) - 1 if len(ans) != 0 else 0)