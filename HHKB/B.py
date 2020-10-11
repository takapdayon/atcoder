def futon(h, w, slist):

    ans = 0

    for i in range(h):
        for q in range(w):
            if q+1 != w:
                if slist[i][q] == "." and slist[i][q+1] == ".":
                    ans += 1
            if i != 0:
                if slist[i][q] == "." and slist[i-1][q] == ".":
                    ans += 1
    return ans

h, w = map(int, input().split())
slist = [list(str(input()))for _ in range(h)]
print(futon(h, w, slist))
