N = int(input())
A = sorted(list(map(int,input().split())))
amari = 10**9 + 7
ans = []
han = 0

if N % 2 == 0:
    han = 1
else:
    han = 0
    A.insert(0,0)


ans = list(int(i) for i in range(han,N,2))
ans += ans
ans.sort()

if ans == A:
    print(2**(N//2) % amari)
else:
    print("0")