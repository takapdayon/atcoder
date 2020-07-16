def d168(n, m, abli):

    ans = []
    count = [0]*n-1
    iki = [0][0]*n

    for i in abli:
        iki[abli[i][0]].append(abli[i][1])
        iki[abli[i][1]].append(abli[i][0])

    for i in range(1,n+1):
        for w in iki[i]:
            if w != 1:
                if count[w] == 0:
                    count[w] == i

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