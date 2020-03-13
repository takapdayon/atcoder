import sys

N, M = map(int, input().split())
if N == 0 or M == 0:
    print("0","0")
    sys.exit()

Clist = [list(input().split()) for _ in range(M)]
ans = 0
answa = 0
acf = 0
pi = Clist[0][0]

if Clist[0][1] == "AC":
    ans += 1

for al in range(M):
    if pi != Clist[al][0]:
        acf = 0
    if acf == 0 and Clist[al][1] == "WA":
        answa += 1
    elif  acf == 0 and Clist[al][1] == "AC":
        ans += 1
        acf = 1
    pi = Clist[al][0]

print(ans,answa)