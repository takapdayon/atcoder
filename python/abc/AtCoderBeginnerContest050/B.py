N = input()
T = list(map(int,input().split()))
M = int(input())

for x in range(M):
    p , x = map(int,input().split())
    a = T[p - 1]
    T[p - 1] = x
    print(sum(T))
    T[p - 1] = a