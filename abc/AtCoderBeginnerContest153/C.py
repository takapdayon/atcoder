import sys

H , A = map(int, input().split())
li = list(map(int,input().split()))

if H <= A:
    print(0)
    sys.exit()

sli = sorted(li, reverse=True)

print(sum(li) - sum(sli[:A]))