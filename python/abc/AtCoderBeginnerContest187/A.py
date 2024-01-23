a, b = map(list, list(input().split()))
asum = sum(map(int, a))
bsum = sum(map(int, b))
print(max(asum, bsum))