def d183(n, w, stplist):

    count = [0]*(2*10**5+1)

    for stp in stplist:
        count[stp[0] - 1] += stp[2]
        count[stp[1] - 1] -= stp[2]

    ans = [0]*(2*10**5+1)
    ans[0] = count[0]
    for i in range(1, len(ans)):
        ans[i] = ans[i-1] + count[i]

    if max(ans) > w:
        return "No"
    else:
        return "Yes"

n, w = map(int, input().split())
stplist = [list(map(int, input().split()))for i in range(n)]
print(d183(n, w, stplist))