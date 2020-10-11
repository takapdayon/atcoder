def neq_min(n, plist):

    ans = []
    klist = set()
    minst = 0

    for i in plist:
        klist.add(i)
        if minst not in klist:
            ans.append(minst)
        else:
            while True:
                if minst not in klist:
                    ans.append(minst)
                    break
                else:
                    minst += 1

    return ans

n = int(input())
plist = list(map(int, input().split()))
pans = neq_min(n, plist)
for i in pans:
    print(i)
