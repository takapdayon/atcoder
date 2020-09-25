def lamp(h, w, slist):

    ans = 0

    width = []
    height = []

    for i in slist:
        tmp = []
        for w in i:
            if w == "#":
                tmp.append("#")
            else:
                tmp.append("")
        width.append(tmp)

    for i in range(w):
        tmp = []
        for w in range(h):
            if slist[w][i] == "#":
                tmp.append("#")
            else:
                tmp.append("")
        height.append(tmp)

    

    return ans

def main():
    h, w = map(int, input().split())
    slist = [list(map(str, input().split()))for i in range(h)]
    print(lamp(h, w, slist))

if __name__ == '__main__':
    main()