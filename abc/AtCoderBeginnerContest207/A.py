abc = list(map(int, input().split()))
abc.sort(reverse=True)
print(abc[0] + abc[1])