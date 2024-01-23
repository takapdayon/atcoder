
def saiki(i, abli, flag):

    ans = 1000
    iki = []
    ret = 0

    if i == 1:
        return 1

    for w in abli:
        if w[0] == i and flag[w[1]-1]:
            iki.append(w[1])

    for w in iki:
        flag[w-1] = False
        count = saiki(w, abli, flag)
        flag[w-1] = True
        if count == 100:
            return 100

        else:
            if ans >= count:
                ans = count
                ret = w

        #親まで帰ってきたときに深さを知りたい and 親側から最初の値を知りたい

    return ret

def d168(n, m, abli):

    ablirev = []
    ans = []
    for i in abli:
        ablirev.append([i[1],i[0]])
    abli = abli+ablirev

    for i in range(2, n+1):
        flag = [True]*n
        ff = saiki(i, abli, flag)

        if ff == 100:
            return "No"

        else:
            ans.append(ff)

    return ans

def main():
    n, m = map(int, input().split())
    abli = [list(map(int, input().split()))for i in range(m)]
    ans = d168(n, m, abli)
    print("Yes")
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()