def c188(n, al):

    ans = 0
    tour1 = max(max(al[::4]), max(al[1::4]))
    tour2 = max(max(al[2::4]), max(al[3::4]))
    second = min(tour1, tour2)
    ans = [i for i, a in enumerate(al) if a == second]
    return ans[0]+1

n = int(input())
al = list(map(int, input().split()))
print(c188(n, al))
