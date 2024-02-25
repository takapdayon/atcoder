import itertools
def c167(n, m, x, cali):

    ans = 10**8
    skill = [0]*m

    for i in cali:
        for w in range(m):
            skill[w] += i[w+1]

    for i in skill:
        if i < x:
            return -1
    for i in range(1, n+1):
        itelist = list(itertools.combinations(range(n),i))
        print(itelist)
        for w in itelist:
            countans = 0
            countskill = [0]*m
            flag = True
            for q in w:
                countans += cali[q][0]
                for g in range(m):
                    countskill[g] += cali[q][g+1]
            for q in countskill:
                if q < x:
                    flag = False
            if flag:
                ans = min(ans, countans)

    return ans

def main():
    n, m, x = map(int, input().split())
    cali = [list(map(int, input().split()))for i in range(n)]
    print(c167(n, m, x, cali))

if __name__ == '__main__':
    main()