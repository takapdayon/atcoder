def b188(n, al, bl):

    ans = 0
    for a, b in zip(al, bl):
        ans += a * b

    return 'Yes' if ans == 0 else 'No'

n = int(input())
al = map(int, input().split())
bl = map(int, input().split())
print(b188(n, al, bl))