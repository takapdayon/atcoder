#??????????????????????
from collections import defaultdict
def vvv(n , vl):

    ans = 0
    gdict = defaultdict(int)
    kdict = defaultdict(int)
    for i in range(n):
        if i % 2 == 0:
            gdict[vl[i]] += 1
        else:
            kdict[vl[i]] += 1

    glist = sorted(list(gdict.items()) , key = lambda x: x[1])
    klist = sorted(list(kdict.items()) , key = lambda x: x[1])

    if int(glist[0][1]) == int(klist[0][1]):
        if int(glist[0][0]) == int(klist[0][0]):
            ans = int(klist[0][1])
    else:
        ans = sum(list(gdict.values())) - int(glist[0][1]) + sum(list(kdict.values())) - int(klist[0][1])

    return ans

def main():
    n = int(input())
    vl = list(map(int , input().split()))
    print(vvv(n , vl))

if __name__ == '__main__':
    main()