#??????????????????????
from collections import defaultdict
def vvv(n , vl):

    ans = 0
    gdict = defaultdict(int)
    kdict = defaultdict(int)
    for i in range(n):
        if i % 2 == 0:
            gdict[str(vl[i])] += 1
        else:
            kdict[str([i])] += 1
    print(gdict)

    glist = sorted(list(gdict) , key = lambda x: x[0])
    klist = sorted(list(kdict) , key = lambda x: x[0])

    print(glist)
    print(klist)

    if int(glist[0][1]) == int(klist[0][1]):
        if int(glist[0][0]) == int(klist[0][0]):
            ans = int(klist[0][1])
    else:
        ans = sum(int(glist[1])) - int(glist[0][1]) + sum(int(klist[1])) - int(klist[0][1])

    return ans

def main():
    n = int(input())
    vl = list(map(int , input().split()))
    print(vvv(n , vl))

if __name__ == '__main__':
    main()