def c166(n, m, hl, abli):

    flag = [True]*n

    for i in abli:
        if hl[i[0]-1] < hl[i[1]-1]:
            flag[i[0]-1] = False
        elif  hl[i[0]-1] == hl[i[1]-1]:
            flag[i[0]-1] = False
            flag[i[1]-1] = False
        else:
            flag[i[1]-1] = False

    ans = flag.count(True)
    return ans

def main():
    n, m = map(int, input().split())
    hl = list(map(int, input().split()))
    abli = [list(map(int, input().split()))for i in range(m)]
    print(c166(n, m, hl, abli))

if __name__ == '__main__':
    main()