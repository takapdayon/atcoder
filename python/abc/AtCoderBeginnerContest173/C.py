def c173(h, w, k, clist):

    ans = 0

    for i in range(h):
        for y in range(w):
            count = 0
            for q in range(h):
                for t in range(w):
                    if i != q and y != t:
                        if clist[q][t] == "#":
                            count += 1
            if count == k:
                ans += 1

    return ans

def main():
    h, w, k = map(int, input().split())
    clist = [list(str(input()))for i in range(h)]
    print(c173(h, w, k, clist))

if __name__ == '__main__':
    main()