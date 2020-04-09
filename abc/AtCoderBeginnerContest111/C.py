#要素数-1と勘違いしてた。明日やります。
def vvv(n , vl):

    ans = 0
    gvl = vl[0::2]
    kvl = vl[1::2]


    if sum(gvl) == sum(kvl) and gvl.count(gvl[0]) == kvl.count(kvl[0]):
        ans = n / 2


    return ans

def main():
    n = int(input())
    vl = list(map(int , input().split()))
    print(vvv(n , vl))

if __name__ == '__main__':
    main()