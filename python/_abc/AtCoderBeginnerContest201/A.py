al = list(map(int, input().split()))
al.sort()
if al[2] - al[1] == al[1] - al[0]:
    print("Yes")
else:
    print("No")