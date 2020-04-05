
def Grid_Compression(h , w , ahl):

    ans = []
    hcount = []
    wcount = []

    for n in range(w):
        flag = True
        for m in range(h):
            if ahl[m][n] == "#":
                flag = False
        if flag == False:
            wcount.append(n)

    for n in range(h):
        flag = True
        for m in range(w):
            if ahl[n][m] == "#":
                flag = False
        if flag == False:
            hcount.append(n)

    for nh in hcount:
        ansli = []
        for nw in wcount:
            ansli.append(ahl[nh][nw])
        ans.append(ansli)

    return ans

def main():
    h , w = map(int , input().split())
    ahl = [list(str(input())) for i in range(h)]
    ans = Grid_Compression(h , w , ahl)
    for i in ans:
        pr = ""
        for w in i:
            pr += w
        print(pr)

if __name__ == '__main__':
    main()